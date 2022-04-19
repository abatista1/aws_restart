import json

def isprime(n):
    for e in range(2,n):
        if n%e == 0:
            return False
    return True
    
def primeslist(numbers):
    primes = []
    for e in numbers:
        if isprime(e):
            primes.append(e)
    return primes 
    
def lambda_handler(event, context):
    numbers = list(range(1,100))     
    primes = primeslist(numbers)

    return {
        'statusCode': 200,
        'body': json.dumps(primes)
    }

