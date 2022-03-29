#!/bin/python3

### Exercise 5 - The IPv4 to Binary Algorithm:

# Read an IPv4 and a CIDR prefix n (0 <= n <= 32) from STDIN. The Python script should do the following:  #INCORRECT - but need to check - CIDR prefix can't be 0 - otherwise there would be 33 values
# -   Convert the IP to Binary and print it out formatted as  xxx.xxx.xxx.xxx
# -   Determine the Network Address based on n and print the Network Address in binary and decimal
# -   Determine the Network Mask based on n and print the Mask Address in binary and decimal
# -   Calculate and print the number of usable subnets for a prefix = (32-n)/2
# -   Based on the above subnets calculate and print the number of usable hosts

# Sample I/O: 

#     IPv4: <xxx.xxx.xxx.xxx>
#     Prefix: <prefix value>
#     Network Binary: <binary value>
#     Network Decimal: <decimal value>
#     Mask Binary: <binary value>
#     Mask Decimal: <decimal value>
#     Usable Subnets: <subnets value>
#     Usable Hosts: <host value>


def check_ip(ip):
    
    valid_octets = 0
    ip_octets = ip.split(".")
    
    # check that there are 4 octects
    if len(ip_octets) < 4:
        return False
    
    # check that each octect is between 0 and 255
    for octet in ip_octecs:
        try:
            o = int(octet)
            if o >= 0 and o <= 255:
                valid_octets += 1      # count the valid octects, we should have 4 if successful
            else:
                break       # no need to check any further
                
        except ValueError:
            break           # no need to check any further
    
    return valid_octets == 4

def read_ip():
    
    while True:
        ip = input("IPv4: ")
        if check_ip(ip):                # make sure it is in a valid format
            break
        else:
            print(f"Invalid IP address format!")
    return ip

def ip_to_string(octet_list):
    
    bin_ip_str = ""
    i = 0
    for o in octet_list:
        bin_ip_str += str(o)
        i += 1
        if i <= 3:
           bin_ip_str += "."
    
    return bin_ip_str
        
        

def convert_ip_to_binary(to_convert):
    ip_octets = to_convert.split(".")
    bin_ip = []
    
    for octet in ip_octets:
        bin_octet = bin(int(octet))
        bin_octet = bin_octet[2:]     # bin returns values starting with ob, so strip these
        bin_octet = bin_octet.zfill(8)    # pad with 0 for 8 characters
        bin_ip.append(bin_octet)           # add to octect list
        # bin_ip.append(bin_octect[2:])   # bin returns values starting with ob, so strip these
                
    return bin_ip

def check_prefix(prefix):
    
    valid = False
    try:
        p = int(prefix)
        if p >= 0 and p <= 32:
            valid = True      # count the valid octects, we should have 4 if successful
    except ValueError:
        pass
    
    return valid

def read_prefix():
    while True:
        prefix = input("Prefix: ")
        if check_prefix(prefix):
            break
        else:
            print(f"Invalid prefix, expecting a value between 0 and 32!")
    return prefix    

def binary_to_dcimal(n):
    return int(n,2)
            
def get_subnet_mask_ip(prefix):
    
    i = 0
    
    bin_subnet_mask_ip = []
    dec_subnet_mask_ip = []
    bin_octet = ""
    subnet_ip_str = ""
    
    while i < 32:
        if i < int(prefix):
            subnet_ip_str += "1"
        else:
            subnet_ip_str += "0"
            
        i += 1
    print(subnet_ip_str)
    
    # break into octets
    bin_octet = subnet_ip_str[0:8]
    bin_subnet_mask_ip.append(bin_octet)
    dec_subnet_mask_ip.append(binary_to_dcimal(bin_octet))
    bin_octet = subnet_ip_str[8:16]
    bin_subnet_mask_ip.append(bin_octet)
    dec_subnet_mask_ip.append(binary_to_dcimal(bin_octet))
    bin_octet = subnet_ip_str[16:24]
    bin_subnet_mask_ip.append(bin_octet)
    dec_subnet_mask_ip.append(binary_to_dcimal(bin_octet))
    bin_octet = subnet_ip_str[24:32]
    bin_subnet_mask_ip.append(bin_octet)
    dec_subnet_mask_ip.append(binary_to_dcimal(bin_octet))
    
    print(ip_to_string(bin_subnet_mask_ip))
    print(ip_to_string(dec_subnet_mask_ip))
    
    return bin_subnet_mask_ip, dec_subnet_mask_ip

    

def get_network_ip(ip, prefix):
    #expects a binary ip in a list
    
    n_ip = []
    
    
    
    
    
    
#     Binary form	Dot-decimal notation
# IP address	11000000.00000000.00000010.10000010	192.0.2.130
# Subnet mask	11111111.11111111.11111111.00000000	255.255.255.0
# Network prefix	11000000.00000000.00000010.00000000	192.0.2.0
# Host identifier	00000000.00000000.00000000.10000010	0.0.0.130
    
    return
    
    
    
            
#dec_ip_str = read_ip()
prefix = read_prefix()
dec_ip_str = "222.222.222.222"
print(dec_ip_str)

bin_ip = convert_ip_to_binary(dec_ip_str)
bin_ip_str = ip_to_string(bin_ip)
print(bin_ip_str)

#prefix = read_prefix()
print(prefix)

bin_subnet_mask_ip, dec_subnet_mask_ip = get_subnet_mask_ip(prefix)     # derive the subnet mask ip in binary & decial



