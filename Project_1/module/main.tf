resource "aws_instance" "web" {
  ami           = var.amis
  instance_type = var.boxtype

  tags = {
    Name = var.tag
  }
}


