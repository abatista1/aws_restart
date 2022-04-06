# AWS DynamoDB CLI:

https://docs.aws.amazon.com/cli/latest/reference/rds/

### Create DynamoDB Tables
```
aws dynamodb create-table
    --table-name <Table-Name>
    --attribute-definitions AttributeName=<Partition-key>,AttributeType=S AttributeName=<Sort-key>,AttributeType=S
    --key-schema AttributeName=<Partition-key>,KeyType=HASH AttributeName=<Sort-key>,KeyType=RANGE
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
    --tags Key=Owner,Value=blueTeam


```

### Show DynamoDB Tables
```
aws dynamodb list-tables 

```

### Describe DynamoDB Table
```
aws dynamodb describe-table --table-name <Table-Name> 

```

### Delete DynamoDB Table
```
aws dynamodb delete-table --table-name students

```

### Fetch DynamoDB Table Items
```
aws dynamodb scan --table-name <Table-Name> 

```

### Write Items to Table
```
aws dynamodb put-item --table-name students --item "{\"Id\":{\"S\":\"789\"},\"name\":{\"S\":\"Mark Shultz\"}}"

or use bulk items from JSON:

aws dynamodb put-item --table-name <Table-Name> --item file://filename.json 

```

### Delete Item from Table
```
aws dynamodb delete-item --table-name students --key "{\"Id\":{\"S\":\"789\"},\"name\":{\"S\":\"Mark Shultz\"}}"

```

### Update Item in Table
```
aws dynamodb update-item --table-name NameOfTheTable 
    --key '{"Id":{"S":"123"}}' 
    --update-expression "SET HomeAddress = :h, DOB = :d" 
        --expression-attribute-values '{":h": { "S": "Menlo Park 1" },":d": { "S": "1234568990" }}' 
        --return-values ALL_NEW

```