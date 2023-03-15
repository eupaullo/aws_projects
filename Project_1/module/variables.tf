variable "tag"{
    type = string
    description = "Please provide a ec2 Tag Name"
    default = "Ec2-webserver"
}

variable "boxtype"{
    type = string
    description = "Intance type for the ec2 instance"
    default = "t2.micro"
}
variable "amis"{
    type = string
    description = "ami for the ec2 instance"
    default = "ami-0b0dcb5067f052a63"
}