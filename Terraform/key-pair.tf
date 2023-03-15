## Generate the Key using tls_private_key resources
## Copy the key to the server using aws_key_pair resources
## Output the private key using output value
## copy the private key to a file and save

// Generate a key 
resource "tls_private_key" "key-pair" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "deployer" {
  key_name   = var.key-pair
  public_key = tls_private_key.key-pair.public_key_openssh

}


output "private_key" {
  value     = tls_private_key.key-pair.private_key_openssh
  sensitive = true
}

