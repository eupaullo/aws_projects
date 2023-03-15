resource "aws_vpc" "test-vpc" {
  cidr_block           = "10.0.0.0/16"
  instance_tenancy     = "default"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name        = "test-vpc",
    Environment = "test",
    team        = "Security",
    MonthCreated = "November",
    Owner = "EUP"
    department = "developer"
  }
}

resource "aws_vpc" "dev-vpc" {
  cidr_block           = "10.0.0.0/16"
  instance_tenancy     = "default"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name        = "Dev-vpc",
    Environment = "test",
    team        = "Security",
    MonthCreated = "November",
    Owner = "EUP"
    department = "developer"
  }
  # lifecycle {
  #   create_before_destroy = true
  # }
}
output "test-vpc-output" {
  value = resource.aws_vpc.test-vpc.cidr_block
}