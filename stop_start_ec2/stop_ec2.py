#Create Python scripts to start and stop EC2 instances, then apply those scripts to Lambda functions. Then use #Amazon EventBridge to schedule the functions so that the EC2 instances start and stop depending on the hours they #should be working.

#Tag the instances you want to stop/start e.g. Environement: Test
#Install AWS CLI and Boto3 e.g. pip install boto3 and pip install awscliv2

#Create Python script to stop the tagged EC2 instances
import boto3
import json

ec2 = boto3.client('ec2', region_name='us-west-1')
#instance = []
def is_test(instance):
    tag = {'Key':'Env', 'Value':'Test1'}
    is_test = False
    if tag in instance['Tags']:
        is_test = True
    return is_test
def is_running(instance):
    is_running = False
    if instance['State']['Name'] == 'running':
        is_running = True
    return is_running
instance_attr = ec2.describe_instances() 

reservations = instance_attr['Reservations'] 

def lambda_handler(event, context):
    for reservation in reservations: 
        for instance in reservation['Instances']: 
            if (is_test(instance) and is_running(instance)): 
                instance_id = instance['InstanceId'] 
                ec2.stop_instances(InstanceIds=[instance_id]) 
                print("The following instance has stopped: " + instance_id)

# if __name__ == "__main__":
#     is_test(instance)
