# variable "sg_ports" {
#   type        = list(number)
#   description = "List of portss"
#   default     = [22, 21, 805, 80, 443]
# }

# resource "aws_security_group" "main_sg" {
#   name        = "dynamic-sg"
#   description = "demo dynamic sg"

#   dynamic "ingress" {
#     for_each = var.sg_ports
#     content {
#       from_port   = ingress.value
#       to_port     = ingress.value
#       protocol    = "tcp"
#       cidr_blocks = ["0.0.0.0/0"]
#     }
#   }
#   tags = {
#     "Name" = "Demo-dynamic"
#   }
# }