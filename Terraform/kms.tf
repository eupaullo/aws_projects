# resource "aws_kms_key" "ami-kms-key" {
#   description             = "KMS key 1"
#   deletion_window_in_days = 10
#   tags = {
#     "Name" = "Terraform-Key"
#   }
# }


resource "aws_instance" "name" {
  ami = var.ami
  instance_type = var.instance_type
  key_name = var.key_name
  iam_instance_profile = var.iam_instance_profile
  availability_zone = var.availability_zone

  lifecycle {
    create_before_destroy = var.create_before_destroy
  }

#   validation = {
#     verify_ami = var.verify_ami
#   }
}