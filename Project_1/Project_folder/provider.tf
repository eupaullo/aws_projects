terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.40.0"
    }
  }
  backend "s3" {
    bucket         = "container123020"
    key            = "dev/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraformbackend"
  }
}


provider "aws" {
  # Configuration options
  region = "us-east-1"
}

