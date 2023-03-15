
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.31.0"
    }
  }
}

provider "aws" {
  # Configuration options
  region  = "us-east-1"
  profile = "vscode"
  default_tags {
    tags = {
      "Environment"  = "Testing"
      "Project_name" = "Datadog-training"
      "Owner"        = "EUP"
    }
  }
}






