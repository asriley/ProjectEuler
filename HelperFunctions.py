# helper functions for Project Euler problem set
# Finds the max in a list
def maxInList (l):
    max = l[0]
    for x in range (1, len(l)):
        if max < l[x]:
            max = l[x]
    return max

# performs an operation on all list elements
def performOpOnList (l, op):
    result = 1
    for x in range(0, len(l)):
        if op==1:
            result = result + l[x]
        else:
            result = result * l[x]
    if op == 1:
        return result -1
    else:
        return result

# all usage of prime factors should resort to this function
def primeFactors (dividend):
    quotient = 2
    divisor = 2
    factorlist = []
    while quotient >= 2:
        if isPrime(divisor) and dividend % divisor == 0:
            quotient = dividend/divisor
            factorlist.append(divisor)
            dividend = quotient
        else:
            divisor = divisor + 1
    return factorlist

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(n ** (0.5)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

# could also just reverse the string and compare to original
def palindrome (x):
    n = str(x)
    leng = len(n)
    half1 = n[0: int(leng/2.0)]
    half2 = n[int(leng/2.0): leng]
    end = -1
    for x in range (0, int(leng/2.0)):
        if half1[x] != half2[end]:
            return False
        end = end - 1
    return True

def problem5_old (ceiling):
    primesBelowCeiling = primeFactors(ceiling);
    start = performOpOnList(primesBelowCeiling, 1);
    stop = 3000 # needs update
    if (start % 2 != 0):
        start = start + 1
    for x in range(start, stop, 2):
        primes = primeFactors(x)
        primes.insert(0,1)
        print (primes)
        highest_found = False
        # determine if a multiplicative match found btw ceiling nums and primes
        for i in range(2,ceiling+1):
            ceiling_found = False
            for j in range(0,len(primes)):
                for k in range(1,len(primes)):
                    if primes[j] * primes[k] == i:
                        ceiling_found = True
                        print ("found for " +str(x) + " "+ str(i) + " " + str(j) + " " + str(k))
                        break
            if ceiling_found == True:
                highest_found = True
            else:
                highest_found = False
        if highest_found == True:
            return x
    return None
