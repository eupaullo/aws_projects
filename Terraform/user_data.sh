#! /bin/bash
sudo yum update -y
cd /var
sudo yum install httpd -y
sudo service httpd start
chkconfig httpd on
sudo service httpd enable
cd www/html
sudo wget https://www.free-css.com/assets/files/free-css-templates/download/page282/pro.zip
sudo unzip pro.zip
sudo mv pro-html/* .
sudo rm -rf pro*
cd ~

System status and instance status

#!/bin/bash
cd /tmp
sudo yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm
sudo systemctl enable amazon-ssm-agent
sudo systemctl start amazon-ssm-agent

#!/bin/bash
sudo su -
sudo yum update -y
cd /tmp
sudo yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm
sudo systemctl enable amazon-ssm-agent
sudo systemctl start amazon-ssm-agent
cd /var
sudo yum install httpd -y
sudo service httpd start
chkconfig httpd on
sudo service httpd enable
cd www/html
sudo echo "<h1>This is our first page</h1>" > index.html
sudo echo "This is order page of MWeb-1" > order.html

### Ubuntu OS
#!/bin/bash
sudo apt-get update
sudo apt-get install apache2 -y
sudo cd /var/www/html
echo "Welcome to Autoscaling tutorial site" > index.html



"S3:GetAccessPoint"
"s3:ListAllMyBuckets"
"s3:ListAccessPoints"
"s3:ListMultiRegionAccessPoints"
"s3:ListBucket"


