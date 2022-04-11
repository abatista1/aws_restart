# Using EC2 CLI:

* https://docs.aws.amazon.com/cli/latest/reference/ec2/

## Process to cleaning up an EC2 environment:

### Step 1: Describe EC2 status
```
aws ec2 describe-instance-status --instance-ids <instance_id>
aws ec2 describe-instances --instance-ids <instance_id>

```

### Step 2: Terminate EC2
```
aws ec2 terminate-instances --instance-ids <instance_id>

```

### Step 3: Detach IGW from VPC
```
aws ec2 detach-internet-gateway 
    --internet-gateway-id <igw-id>
    --vpc-id <vpc-id>

```

### Step 4: Delete IGW
```
aws ec2 delete-internet-gateway 
    --internet-gateway-id <igw-id>

```

### Step 5: Delete Subnet
```
aws ec2 delete-subnet --subnet-id <subnet-id>

```

### Step 6: Deassociate Route Table
```
aws ec2 disassociate-route-table --association-id <associate-id> 

```

### Step 7: Delete Route Table
```
aws ec2 delete-route-table --route-table-id <rt-id>

```

### Step 8: Delete SG
```
aws ec2 delete-security-group --group-id <sg-id>
aws ec2 delete-security-group --group-name <group-name>

```

### Step 9: Delete key-pair
```
aws ec2 delete-key-pair --key-name <keypair-name>

```

### Step 10: Release an Elastic IP
```
aws ec2 release-address --public-ip <EIP>

```

### Step 11: Release an Elastic IP for EC2 VPC 
```
aws ec2 release-address --allocation-id <allocation-id>

```

### Step 12: Delete Nat Gatway
```
aws ec2 delete-nat-gateway --nat-gateway-id <nat-gw-id>

```

### Step 13: Delete ENI
```
aws ec2 delete-network-interface 
    --network-interface-id <eni-id>

```

### Step 14: Delete VPC
```
aws ec2 delete-vpc --vpc-id <vpc-id>

```
