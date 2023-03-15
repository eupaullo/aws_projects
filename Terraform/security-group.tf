resource "aws_security_group" "allow_sg" {
  name        = "prima-cloud-sg"
  description = "Allow ssh,http and https inbound traffic"
  vpc_id      = var.vpc.id

  dynamic "ingress" {
    for_each = var.ports
    content {
      description = "prima port"
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "Prima-cloud-sg"
  }
}