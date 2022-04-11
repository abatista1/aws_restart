## EC2 Access Using SSH

* Create an EC2 instance using AWS Management Console or AWS CLI
* Save the <code>.pem</code> keypair on your local PC
  
### SSH From Your PC to the EC2 instance:

```
$ ssh -i "file.pem" ec2-user@hostname

```

### Copy Files From Your PC to EC2 using SCP:

```
scp -i file.pem filename ec2-user@hostname:~

scp -i file.pem -r folder ec2-user@hostname:~/path/to/remote/destination 


```

### Copy Files From EC2 to your PC using SCP:

```
scp -r ec2-user@hostname:/path/to/remote/source /path/to/local/destination
```

## Demo: Update EC2 userdata using SCP

### Given we create an EC2 instance with user-data field
```
#!/bin/bash
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html

```

### We want to update the index.html on the running EC2
* First: copy index.html from local PC to EC2 home using scp
```
scp -i file.pem index.html ec2-user@hostname:~

```
* Second: overwrite index.html in /var/www/html on EC2 with the newly uploaded version
```
sudo cp index.html /var/www/html/index.html

```


### To Fix SSH Permission denied (publickey,gssapi-keyex,gssapi-with-mic):
* Stop the EC2 instance
* From Actions choose Instance Settings and then select Edit User Data
* Copy the following script into the User Data and then choose Save.
* Replace the value for OS_USER with the user name associated with the EC2.
```
#!/bin/bash
OS_USER=@@@@@@
chown root:root /home 
chmod 755 /home
chown $OS_USER:$OS_USER/home/$OS_USER -R
chmod 700 /home/$OS_USER
chmod 700 /home/$OS_USER/.ssh
chmod 600 /home/$OS_USER/.ssh/authorized_keys

```

