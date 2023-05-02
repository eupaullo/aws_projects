import boto3
import json




def stopInstance():
    """
    Stops an EC2 instance that has been idle for 5 minutes or more.

    Parameters:
    event (dict): AWS Lambda event data.
    context (object): AWS Lambda context object.

    Returns:
    None

    Raises:
    None
    """

    # Initialize the EC2 client
    ec2 = boto3.client('ec2')

    # Get the list of instances in the account
    response = ec2.describe_instances() # GIVE US ALL THE LIST OF THE INSTANCES IN OUT ACCOUNT
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            # Get the last time the instance was launched
            launch_time = instance["LaunchTime"]
            current_time = datetime.datetime.now(launch_time.tzinfo)
            # Calculate the time difference in minutes
            diff_minutes = (current_time - launch_time).total_seconds() / 60.0
            # Check if the instance has been idle for 5 minutes
            if instance["State"]["Name"] == "running" and diff_minutes >= 60:
                # Stop the instance
                ec2.stop_instances(InstanceIds=[instance["InstanceId"]])
                # Print the instance that has been stopped
                print(f"Instance {instance['InstanceId']} has been stopped.")
    Print response in JSON format
    print(json.dumps(response, default= str,  indent=4))
    # print(response)


    # return None
stopInstance()
