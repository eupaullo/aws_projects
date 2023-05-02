response =  {
    "Reservations": [
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-007855ac798b5175e",
                    "InstanceId": "i-058efd11f07b4d119",
                    "InstanceType": "t2.medium",
                    "KeyName": "EC2-KP",
                    "LaunchTime": "2023-04-23 21:17:54+00:00",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "us-east-1b",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-0-23-178.ec2.internal",
                    "PrivateIpAddress": "10.0.23.178",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2023-04-25 00:40:13 GMT)",
                    "SubnetId": "subnet-066029be01cae55ab",
                    "VpcId": "vpc-0a18955cd3b811c60",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2023-04-21 03:17:45+00:00",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-06deda71f723d69e1"
                            }
                        }
                    ],
                    "ClientToken": "379c2031-8075-4d7d-9c1d-0442a934381e",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "IamInstanceProfile": {
                        "Arn": "arn:aws:iam::406001585564:instance-profile/EC2AdministrativeAccess",
                        "Id": "AIPAV5B4URWODHQ7AJLUR"
                    },
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2023-04-21 03:17:44+00:00",
                                "AttachmentId": "eni-attach-00e24b040691986ca",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached",
                                "NetworkCardIndex": 0
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "Dev-SG",
                                    "GroupId": "sg-0d469be4624db9495"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "0a:7d:1f:8b:86:97",
                            "NetworkInterfaceId": "eni-03b207ef8510f7104",
                            "OwnerId": "406001585564",
                            "PrivateDnsName": "ip-10-0-23-178.ec2.internal",
                            "PrivateIpAddress": "10.0.23.178",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-0-23-178.ec2.internal",
                                    "PrivateIpAddress": "10.0.23.178"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-066029be01cae55ab",
                            "VpcId": "vpc-0a18955cd3b811c60",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "Dev-SG",
                            "GroupId": "sg-0d469be4624db9495"
                        }
                    ],
                    "SourceDestCheck": True,
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "docker"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 2,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled",
                        "HttpProtocolIpv6": "disabled",
                        "InstanceMetadataTags": "disabled"
                    },
                    "EnclaveOptions": {
                        "Enabled": False
                    },
                    "PlatformDetails": "Linux/UNIX",
                    "UsageOperation": "RunInstances",
                    "UsageOperationUpdateTime": "2023-04-21 03:17:44+00:00",
                    "PrivateDnsNameOptions": {
                        "HostnameType": "ip-name",
                        "EnableResourceNameDnsARecord": False,
                        "EnableResourceNameDnsAAAARecord": False
                    },
                    "MaintenanceOptions": {
                        "AutoRecovery": "default"
                    }
                }
            ],
            "OwnerId": "406001585564",
            "ReservationId": "r-031bb552c0c04d42c"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-02396cdd13e9a1257",
                    "InstanceId": "i-05a5c61d80f324b7d",
                    "InstanceType": "t2.micro",
                    "KeyName": "EC2-KP",
                    "LaunchTime": "2023-04-23 00:43:48+00:00",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "us-east-1a",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-172-31-82-96.ec2.internal",
                    "PrivateIpAddress": "172.31.82.96",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2023-04-23 00:48:47 GMT)",
                    "SubnetId": "subnet-0e7722c720a5dda54",
                    "VpcId": "vpc-018a0258b41b7b91a",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/xvda",
                            "Ebs": {
                                "AttachTime": "2023-04-23 00:43:49+00:00",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-0bf642139fb59e23b"
                            }
                        }
                    ],
                    "ClientToken": "8acdc2e8-540f-4d85-8c2f-6167d9a60dd5",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2023-04-23 00:43:48+00:00",
                                "AttachmentId": "eni-attach-0edeba0138828770d",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached",
                                "NetworkCardIndex": 0
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "launch-wizard-20",
                                    "GroupId": "sg-051a42266ae5935a5"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "12:51:4f:88:6c:b3",
                            "NetworkInterfaceId": "eni-02d5955f5092ef119",
                            "OwnerId": "406001585564",
                            "PrivateDnsName": "ip-172-31-82-96.ec2.internal",
                            "PrivateIpAddress": "172.31.82.96",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-172-31-82-96.ec2.internal",
                                    "PrivateIpAddress": "172.31.82.96"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-0e7722c720a5dda54",
                            "VpcId": "vpc-018a0258b41b7b91a",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/xvda",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "launch-wizard-20",
                            "GroupId": "sg-051a42266ae5935a5"
                        }
                    ],
                    "SourceDestCheck": True,
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "Jenkins"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 1,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "required",
                        "HttpPutResponseHopLimit": 2,
                        "HttpEndpoint": "enabled",
                        "HttpProtocolIpv6": "disabled",
                        "InstanceMetadataTags": "disabled"
                    },
                    "EnclaveOptions": {
                        "Enabled": False
                    },
                    "BootMode": "uefi-preferred",
                    "PlatformDetails": "Linux/UNIX",
                    "UsageOperation": "RunInstances",
                    "UsageOperationUpdateTime": "2023-04-23 00:43:48+00:00",
                    "PrivateDnsNameOptions": {
                        "HostnameType": "ip-name",
                        "EnableResourceNameDnsARecord": True,
                        "EnableResourceNameDnsAAAARecord": False
                    },
                    "MaintenanceOptions": {
                        "AutoRecovery": "default"
                    }
                }
            ],
            "OwnerId": "406001585564",
            "ReservationId": "r-0067f6d7f87981554"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-02396cdd13e9a1257",
                    "InstanceId": "i-020f17199f8dea673",
                    "InstanceType": "t2.micro",
                    "KeyName": "EC2-KP",
                    "LaunchTime": "2023-04-23 00:41:53+00:00",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "us-east-1a",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-172-31-85-115.ec2.internal",
                    "PrivateIpAddress": "172.31.85.115",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2023-04-23 00:43:17 GMT)",
                    "SubnetId": "subnet-0e7722c720a5dda54",
                    "VpcId": "vpc-018a0258b41b7b91a",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/xvda",
                            "Ebs": {
                                "AttachTime": "2023-04-23 00:41:54+00:00",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-0c4d4b1fc4d1b7ca1"
                            }
                        }
                    ],
                    "ClientToken": "3918f412-9843-4049-a870-9ec237e44b3b",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2023-04-23 00:41:53+00:00",
                                "AttachmentId": "eni-attach-03bc07a280b5d0772",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached",
                                "NetworkCardIndex": 0
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "launch-wizard-19",
                                    "GroupId": "sg-0cb6f56daeba7c0a0"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "12:fb:34:ba:79:9b",
                            "NetworkInterfaceId": "eni-0fa9417191655aa21",
                            "OwnerId": "406001585564",
                            "PrivateDnsName": "ip-172-31-85-115.ec2.internal",
                            "PrivateIpAddress": "172.31.85.115",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-172-31-85-115.ec2.internal",
                                    "PrivateIpAddress": "172.31.85.115"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-0e7722c720a5dda54",
                            "VpcId": "vpc-018a0258b41b7b91a",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/xvda",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "launch-wizard-19",
                            "GroupId": "sg-0cb6f56daeba7c0a0"
                        }
                    ],
                    "SourceDestCheck": True,
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "Ansible"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 1,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "required",
                        "HttpPutResponseHopLimit": 2,
                        "HttpEndpoint": "enabled",
                        "HttpProtocolIpv6": "disabled",
                        "InstanceMetadataTags": "disabled"
                    },
                    "EnclaveOptions": {
                        "Enabled": False
                    },
                    "BootMode": "uefi-preferred",
                    "PlatformDetails": "Linux/UNIX",
                    "UsageOperation": "RunInstances",
                    "UsageOperationUpdateTime": "2023-04-23 00:41:53+00:00",
                    "PrivateDnsNameOptions": {
                        "HostnameType": "ip-name",
                        "EnableResourceNameDnsARecord": True,
                        "EnableResourceNameDnsAAAARecord": False
                    },
                    "MaintenanceOptions": {
                        "AutoRecovery": "default"
                    }
                }
            ],
            "OwnerId": "406001585564",
            "ReservationId": "r-060de02b0667d1743"
        }
    ],
    "ResponseMetadata": {
        "RequestId": "2bb7b447-4b3c-441c-8790-49d1915c911a",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "2bb7b447-4b3c-441c-8790-49d1915c911a",
            "cache-control": "no-cache, no-store",
            "strict-transport-security": "max-age=31536000; includeSubDomains",
            "vary": "accept-encoding",
            "content-type": "text/xml;charset=UTF-8",
            "transfer-encoding": "chunked",
            "date": "Tue, 25 Apr 2023 00:42:23 GMT",
            "server": "AmazonEC2"
        },
        "RetryAttempts": 0
    }
}

item = response['Reservations'][2]['Instances'][0].get('Kansas')
print(item)
