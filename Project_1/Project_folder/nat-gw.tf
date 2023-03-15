resource "aws_eip" "test" {

  count = 2
}


resource "aws_nat_gateway" "database" {
  allocation_id = aws_eip.test[0].id
  subnet_id     = aws_subnet.test-private-subnet4-1a.id
  tags = {
    Name = "NATGW database"
  }

  depends_on = [aws_eip.test]
}

resource "aws_nat_gateway" "database-cache" {
  allocation_id = aws_eip.test[1].id
  subnet_id     = aws_subnet.test-private-subnet4-1a.id
  tags = {
    Name = "NATGW Cache"
  }

  depends_on = [aws_eip.test]
}