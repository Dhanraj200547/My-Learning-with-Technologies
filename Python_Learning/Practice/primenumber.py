def isprime(n):
    prime = True
    for i in range(2,n):
        if n % i == 0:
            prime = False
            break
    return prime

n = 20
for i in range(2,n):
    if isprime(i):
        print(i,end=" ")