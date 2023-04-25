#Create Python scripts to start  EC2 instances, then apply those scripts to Lambda functions. Then use #Amazon EventBridge to schedule the functions so that the EC2 instances start depending on the hours they #should be working.

#Tag the instances you want to start e.g. Environement: Test
#Install AWS CLI and Boto3 e.g. pip install boto3 and pip install awscliv2

#Create Python script to start the tagged EC2 instances
import boto3

ec2 = boto3.client('ec2', region_name='us-west-1')

def is_test(instance):
    tag = {'Key':'Env', 'Value':'Test1'}
    is_test = False
    if tag in instance['Tags']:
        is_test = True
    return is_test

def is_stopped(instance):
    is_stopped = False
    if instance['State']['Name'] == 'stopped':
        is_stopped = True
    return is_stopped

instance_attr = ec2.describe_instances() 

reservations = instance_attr['Reservations'] 

def lambda_handler(event, context):
    for reservation in reservations: 
        for instance in reservation['Instances']: 
            if (is_test(instance) and is_stopped(instance)): 
                instance_id = instance['InstanceId'] 
                ec2.start_instances(InstanceIds=[instance_id]) 
                print("The following instance has started: " + instance_id)