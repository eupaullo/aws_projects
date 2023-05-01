# Assuming that you have already set up your Terraform infrastructure to create an SNS topic, an AWS EventBridge rule, and a Lambda function that triggers on the rule, you can use this code as the Lambda function for the rule. The Lambda function will be triggered whenever a new EC2 instance is launched, and it will send a message to the SNS topic with the instance ID and user identity.
# Note that you will need to set the SNS_TOPIC_ARN environment variable for the Lambda function to the ARN of your SNS topic. You can do this either in the Lambda function's configuration or using Terraform.


import boto3
import json

# Launch the EC2 instance
ec2 = boto3.client('ec2', region_name='us-west-1')
instance = ec2.run_instances(
    ImageId='ami-085284d24fe829cd0',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    # KeyName='my-key-pair',
    # SecurityGroupIds=['sg-12345678'],
    UserData='''#!/bin/bash
                echo "Hello World" >> /tmp/helloworld.txt''',
)
# Extract instance ID and user identity
instance_id = instance['Instances'][0]['InstanceId']
user_identity = boto3.client('sts').get_caller_identity().get('Arn')

def lambda_handler(event, context):
    # Get the details of the new EC2 instance
    instance_id = event['detail']['instance-id']
    response = ec2.describe_instances(InstanceIds=[instance_id])
    instance = response['Reservations'][0]['Instances'][0]
    user_identity = instance['IamInstanceProfile']['Arn']
    
    # Get the SNS topic ARN from the environment variables
    topic_arn = os.environ['arn:aws:sns:us-west-1:274813024103:ec2-provisioning-topic']
    
    # Create a message for the SNS notification
    message = {
        "instanceId": instance_id,
        "userIdentity": user_identity
    }
    
    # Send the message to the SNS topic
    sns = boto3.client('sns', region_name='us-west-1')
    response = sns.publish(
        TopicArn='arn:aws:sns:us-west-1:274813024103:ec2-provisioning-topic',
        Message=json.dumps({'default': json.dumps(message)}),
        MessageStructure='json'
    )
        
# Send the message to the SNS topic
# Create a message for the SNS notification
message = {
    "instanceId": instance_id,
    "userIdentity": user_identity
}

sns = boto3.client('sns', region_name='us-west-1')
response = sns.publish(
    TopicArn='arn:aws:sns:us-west-1:274813024103:ec2-provisioning-topic',
    Message=json.dumps({'default': json.dumps(message)}),
    MessageStructure='json'
)

print(f"Instance {instance_id} launched and notification sent to SNS topic {response['MessageId']}.")
