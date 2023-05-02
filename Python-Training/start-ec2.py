import boto3

def startInstance():
    # Instantiate EC2 client
    ec2 = boto3.client('ec2')
    
    # Specify the parameters for the new instance
    instance_type = 't2.micro'
    ami_id = 'ami-007855ac798b5175e'
    key_name = 'EC2-KP'
    security_group_id = 'sg-0d469be4624db9495'
    subnet_id = 'subnet-0a0e5aa3aff898ab7'
    MinCount = 1
    MaxCount = 1
    
    # Launch the instance
    response = ec2.run_instances(
        InstanceType=instance_type,
        ImageId=ami_id,
        KeyName=key_name,
        SecurityGroupIds=[security_group_id],
        SubnetId=subnet_id,
        MinCount=MinCount,
        MaxCount = MaxCount
    )
    
    # Get the instance ID
    instance_id = response['Instances'][0]['InstanceId']
    
    # Return the instance ID
    print('Instance {} created successfully'.format(instance_id))
    print(f'Instance {instance_id} created successfully')

startInstance()