# assign a name to our VPC

vpc.create_tags(Tags=[{"Key": "Name", "Value": "my_vpc"}])

vpc.wait_until_available()
