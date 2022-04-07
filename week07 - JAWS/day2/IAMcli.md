## Using AWS IAM from CLI

* https://docs.aws.amazon.com/cli/latest/reference/iam/

### List IAM Groups:
```
aws iam list-groups

```

### List IAM users:
```
aws iam list-users

```

### List Group Inline Policies
```
aws iam list-group-policies --group-name <group-name>

```

### List User Inline Policies
```
aws iam list-user-policies --user-name <username>

```

### Create IAM Group
```
aws iam create-group --group-name <group-name>

```

### Attach Policy to Group
```
aws iam attach-group-policy --policy-arn <po;icy-arn> --group-name Marketing

```

### Create IAM User
```
aws iam create-user --user-name <user-name>

```

### Add User to Group
```
aws iam add-user-to-group --user-name <user-name> --group-name <group-name>

```

### Attach Policy to User
```
aws iam attach-user-policy --policy-arn <policy-arn> --user-name <user-name>

```

### Remove User from Group
```
aws iam remove-user-from-group --user-name <user-name> --group-name <group-name>

```

### Detach User Policy
```
aws iam detach-user-policy --user-name Bob --policy-arn <policy-arn>

```

### Delete a User
```
aws iam delete-user --user-name <user-name>

```


### Detach Group Policy
```
aws iam detach-group-policy --group-name Testers --policy-arn <policy-arn>

```

### Delete IAM Group
```
aws iam delete-group --group-name <group-name>

```



