# Create a new EC2 instance using Boto3
import boto3
# How to create an EC2 Instance using Boto3
ec2_instance = boto3.client('ec2', region_name='us-west-1')

response = ec2_instance.run_instances(
    ImageId='ami-09c5c62bac0d0634e',
    InstanceType='t2.micro',
    KeyName='gitlab-runner',
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'TEST'
                },
                {
                    'Key': 'Env',
                    'Value': 'Test1'
                }
            ]
        }
    ]
    #instance.create_tags(Resources=['instance.id'],Tags=[{'Key':'Name', 'Value':'Test'}, {'Key':'Env', 'Value':'Test1'}]) 
  
    )
#ec2_instance.create_tags(Resources=['instance.id'],Tags=[{'Key':'Name', 'Value':'Test'}, {'Key':'Env', 'Value':'Test1'}]) 
print("You have successfully created a new EC2 Instance using BOTO3!")