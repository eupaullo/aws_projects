module "ec2-custom-module" {
  source = "../module/"  
  tag = "web server 9"
  boxtype =  "t2.nano"
}