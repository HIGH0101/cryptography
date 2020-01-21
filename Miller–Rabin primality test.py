# This is a primality test according to miller _robin algorithm
# This implementation is based on description in Secret History
# - The Story of Cryptology book page 465
import random
import time
def is_prime(num):
    if num <= 1:
        return 'No Prime' 
    if num % 2==0: 
        return 'No prime'
    if num==2: 
        return 'prime'  
    s=num-1
    tmp=0
    prime=None
    while tmp%2==0:
        t+=1
        tmp//=2
    d=(num-1)//(2**t)
    print(d)
    a=random.randint(2,num)
    x=pow(a,d,num)
    if x==1:
        prime=True
    for s in range(t): # In python the range function is in [0,t-1) 
        x=pow(a,(2**s)*d,num)
        if x==num-1:   # In madular mathematic x=-1(mod n) is similar to x=n-1(mod n)
            prime=True
    if prime==True:
        return 'prime'
    else:
        return 'No prime'

if __name__=='__main__':
    start = time.time()   
    print(is_prime(22953686867719691230002707821868552601124472329079))
    end = time.time()
    print('execution time : ',abs(start-end))

