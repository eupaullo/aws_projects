data "aws_internet_gateway" "test-igw" {
  internet_gateway_id = var.igw.id
}

output "test_data_gtw" {
  value = data.aws_internet_gateway.test-igw.arn
}