provider "aws" {
  region = "us-east-2"
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.14.4"

  name = "bastion-vpv"
  cidr = "10.0.0.0/16"

  azs             = ["us-east-2a"]
  private_subnets = ["10.0.1.0/24"]
  public_subnets  = ["10.0.101.0/24"]

  enable_nat_gateway = false
  enable_vpn_gateway = false

  tags = {
    Terraform = "true"
    Environment = "dev"
  }

}


module "bastion" {
  source  = "umotif-public/bastion/aws"
  version = "2.4.0"
  region = "us-east-2"
  # insert the 4 required variables here

  name_prefix = "bastion"

  vpc_id         = module.vpc.vpc_id
  public_subnets  = module.vpc.public_subnets
  bastion_instance_types = [ "t4g.micro" ]
  ssh_key_name = "nagios-server"


  hosted_zone_id = ""


  tags = {
    Project = "Test"
  }
}

