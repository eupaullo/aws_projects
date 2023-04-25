import json
import boto3


ec2 = boto3.resource('ec2', region_name='us-west-1')

def stopped_environment_instances(ec2):
    running_environment_instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']},{'Name': 'tag:Env','Values':['Test1']}])
    for instance in running_environment_instances:
        id=instance.id
        ec2.instances.filter(InstanceIds=[id]).stop()
print("All Environment:Test1 Instances are now stopped.")
print("All other environment instances are still running.")
    
if __name__ == "__main__":
    stopped_environment_instances(ec2)