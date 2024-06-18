def is_prime(num):
    prime_number=[]
    for i in range(1,num+1):
        if num%i==0:
            prime_number.append(num)
        if len(prime_number)==2:
            print(f'(num) is a prime number')
        else:
            print(f'(num) is not prime number')
is_prime(10)