# Using EC2 CLI:

* https://docs.aws.amazon.com/cli/latest/reference/ec2/

## Process to creating an EC2 instance:

### Step 1: Create a VPC and configure a CIDR block
```
aws ec2 create-vpc --cidr-block 10.0.0.0/16

```

### Step 2: Create 2 subnets from the CIDR
```
aws ec2 create-subnet --vpc-id <vpcId> --cidr-block 10.0.1.0/24   

aws ec2 create-subnet --vpc-id <vpcId> --cidr-block 10.0.0.0/24   

```

### Step 3: Create Internet Gateway
```
aws ec2 create-internet-gateway

```

### Step 4: Attach the IGW to the VPC
```
aws ec2 attach-internet-gateway 
    --vpc-id <vpcId> 
    --internet-gateway-id <InternetGatewayId>

```

### Step 5: Create Route Table
```
aws ec2 create-route-table --vpc-id <vpcId>  

```

### Step 6: Configure the Route Table and associate it with the IGW
```
aws ec2 create-route 
    --route-table-id <RouteTableId> 
    --destination-cidr-block 0.0.0.0/0 
    --gateway-id <InternetGatewayId>

* View the Route Table (Optional):
aws ec2 describe-route-tables --route-table-id <RouteTableId>

```

### Step 7: Associate the table with a Subnet
```
aws ec2 associate-route-table 
    --subnet-id <SubnetId> 
    --route-table-id <RouteTableId>

```

### Step 8: Map the public IP to a Subnet to make it public
```
aws ec2 modify-subnet-attribute 
    --subnet-id <SubnetId> 
    --map-public-ip-on-launch

```

### Step 9: Create Key Pair and save it to local drive 
```
aws ec2 create-key-pair 
    --key-name AWS-Keypair 
    --query "KeyMaterial" 
    --output text > "\path\filename.pem"

```

### Step 10: Create SG and associate it with the VPC 
```
aws ec2 create-security-group 
    --group-name <security-group-name> 
    --description "<description>" 
    --vpc-id <vpcId>

```

### Step 11: Configure SG
```
aws ec2 authorize-security-group-ingress 
    --group-id <GroupId> 
    --protocol tcp 
    --port 22 
    --cidr 0.0.0.0/0

```

### Step 12: Get recent AMI ID
```
aws ec2 describe-images 
    --owners amazon 
    --filters "Name=name,Values=amzn2-ami-hvm-2.0.????????.?-x86_64-gp2" "Name=state,Values=available" 
    --query "reverse(sort_by(Images, &Name))[:1].ImageId" 
    --region sa-east-1 
    --output text

```

### Step 13: Run the EC2 instance
```
aws ec2 run-instances 
    --image-id <ami-id> 
    --count 1 
    --instance-type t2.micro 
    --key-name <Keypair-name> 
    --security-group-ids <SecurityGroupId> 
    --subnet-id <SubnetId>

```

### Step 14: Verify EC2 status
```
aws ec2 describe-instances --instance-id <InstanceId>

```

### Step 15: Allocate Elastic IP (optional for EIP)
```
aws ec2 describe-instances --instance-id <InstanceId>

```

### Step 16: Associate EIP with EC2 in VPC (optional for EIP)
```
aws ec2 associate-address 
    --instance-id <InstanceId> 
    --public-ip <EIP>

```

### Step 17: Associate EIP with EC2 in ENI (optional for EIP)
```
aws ec2 associate-address 
    --allocation-id <eip-allocation-id> 
    --network-interface-id <eni-id>

```

### Step 17: Create a public NAT Gatway (optional for EIP)
* Associate the NAT GW with EIP to make it public subnet
```
aws ec2 create-nat-gateway 
    --subnet-id <subnet-id> 
    --allocation-id <eip-allocation-id>

```

### Step 17: Create a private NAT Gatway (optional)

```
aws ec2 create-nat-gateway 
    --subnet-id <subnet-id>
    --connectivity-type private

```
