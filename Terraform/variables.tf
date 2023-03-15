variable "ports" {
  type = list(number)
  default = [22, 80, 443, 0-6]
  decription = "dynamic ingress ports"
}
dynamic ingress {
  for_each = var.ports 
  description = "datadog port"
  from_port = ingress.value 
  to_port = ingress.value 
  protocol = "tcp" 
  cidr_blocks = ["172.31.0.0/16"]
}
data "civo_dns_domain_name" "domain" {
  name = "domain.com"
}

output "domain_output" {
  value = data.civo_dns_domain_name.domain.name
}
output "domain_id_output" {
  value = data.civo_dns_domain_name.domain.id
}

