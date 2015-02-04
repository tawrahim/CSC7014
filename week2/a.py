#!/usr/bin/env python
#n = 1
#while True:
    #factors =(i for i in range(1,n) if n%i == 0) #use a generator expression
    #if sum(factors) == n: 
        #print(n)
    #n += 1
def is_magic(n):
    acc = 0
    for i in range(1, n):
        if (n % i == 0):
            acc += i
    if (acc == n):
        return True
    else:
        return False
n = 7
print (is_magic(n))
