terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.30.0"
    }
  }
}

provider "aws" {
  # Configuration options
  region     = "us-east-1"
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_instance" "web-serve" {
    count = 3
    ami = "ami-02538f8925e3aa27a"
    availability_zone = "us-east-1a"
    instance_type = "t2.micro"
    key_name = "Demo-Saturday-key"
    tags = {
      "Name" = "Terraform-Ec2 ${count.index}"
    }
}

output "ip" {
  value = aws_instance.web-server[*].public_ip
}

output "id" {
  value = aws_instance.web-server[*].id
}

output "combined" {
  value =zipmap(aws_instance.web-server[*].public_ip, aws_instance.web-server[*].id)
}
# variable "name" {
#   type = string
# }

# resource "aws_security_group" "allow_tls" {
#   name        = "demo-SG"
#   description = "Allow TLS inbound traffic"
#   vpc_id      = aws_vpc.main.id

#   ingress {
#     description      = "TLS from VPC"
#     from_port        = 443
#     to_port          = 443
#     protocol         = "tcp"
#     cidr_blocks      = [aws_vpc.main.cidr_block]
#   }


#   ingress {
#     description      = "TLS from VPC"
#     from_port        = 22
#     to_port          = 22
#     protocol         = "tcp"
#     cidr_blocks      = [aws_vpc.main.cidr_block]
#   }
#   egress {
#     from_port        = 0
#     to_port          = 0
#     protocol         = "-1"
#     cidr_blocks      = ["0.0.0.0/0"]
#     ipv6_cidr_blocks = ["::/0"]
#   }

#   tags = {
#     Name = var.name
#   }
# }