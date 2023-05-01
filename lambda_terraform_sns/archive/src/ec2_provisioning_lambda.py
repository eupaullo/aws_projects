# This code uses the Boto3 library to launch an EC2 instance with the specified parameters, and then extracts the instance ID and user identity from the response. It then sends a notification to an SNS topic with the instance ID and user identity, using the sns.publish() method. The message sent to the SNS topic is a JSON-encoded string containing the instance ID and user identity. Finally, the code prints a message indicating that the instance was launched and the notification was sent to the SNS topic. Note that you'll need to replace the placeholder values in this code (such as the image ID, key pair name, security group ID, and SNS topic ARN) with your own values.

import boto3
import json

# Initialize Boto3 client
ec2 = boto3.client('ec2')
sns = boto3.client('sns')

# Launch the EC2 instance
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

# Send a notification to the SNS topic
sns_message = {
    'instance_id': instance_id,
    'user_identity': user_identity,
}
response = sns.publish(
    TopicArn='aws_sns_topic.ec2_provisioning_topic.arn',
    Message=json.dumps(sns_message),
)

print(f"Instance {instance_id} launched and notification sent to SNS topic {response['MessageId']}.")

