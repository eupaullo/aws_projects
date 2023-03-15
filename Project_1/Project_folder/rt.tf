# ==================================================
# test-web-sb
# ==================================================

resource "aws_route_table" "test-web-rt" {
  vpc_id = aws_vpc.test-vpc.id
  tags = {
    Name = "test-web-sb"
  }
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = data.aws_internet_gateway.test-igw.id
  }
}


# Subnet Association
# -=====================

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.test-public-subnet-1a.id
  route_table_id = aws_route_table.test-web-rt.id
}

# =========================================================
#  test-app-sb-1 
# =====================================================
## This is a route table for testuction application 1
resource "aws_route_table" "test-app-rt-1" {
  vpc_id = aws_vpc.test-vpc.id
  tags = {
    Name = "test-app-rt-1 "
  }
}


# Subnet Association
# -=====================

resource "aws_route_table_association" "b" {
  subnet_id      = aws_subnet.test-web-sb.id
  route_table_id = aws_route_table.test-app-rt-1.id
}

# =========================================================
#   test-app-sb-2 
# =====================================================
## This is a route table for testuction application 1
resource "aws_route_table" "test-app-rt-2" {
  vpc_id = aws_vpc.test-vpc.id
  tags = {
    Name = "test-app-rt-2 "
  }
}

# Subnet Association
# -=====================
resource "aws_route_table_association" "c" {
  subnet_id      = aws_subnet.test-private-subnet2-1a.id
  route_table_id = aws_route_table.test-app-rt-2.id
}


# =========================================================
#  test-db-cache-rt
# =====================================================
## This is a route table for testuction application 1
resource "aws_route_table" "test-db-cache-rt" {
  vpc_id = aws_vpc.test-vpc.id
  tags = {
    Name = "test-db-cache-rt"
  }
}

# Subnet Association
# -=====================
resource "aws_route_table_association" "d" {
  subnet_id      = aws_subnet.test-private-subnet3-1a.id
  route_table_id = aws_route_table.test-db-cache-rt.id
}

# =========================================================
#  test-db-sb
# =====================================================
## This is a route table for testuction application 1
resource "aws_route_table" "test-db-sb" {
  vpc_id = aws_vpc.test-vpc.id
  tags = {
    Name = "test-db-sb1"
  }
}

# Subnet Association
# -=====================
resource "aws_route_table_association" "e" {
  subnet_id      = aws_subnet.test-private-subnet4-1a.id
  route_table_id = aws_route_table.test-db-sb.id
}