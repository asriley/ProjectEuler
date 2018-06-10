# helper functions for Project Euler problem set
def problem5_old (ceiling):
    primesBelowCeiling = primeFactors(ceiling);
    start = performOpOnList(primesBelowCeiling, 1);
    stop = 3000 # needs update
    if (start % 2 != 0):
        start = start + 1
    for x in range(start, stop, 2):
        primes = primeFactors(x)
        primes.insert(0,1)
        print primes
        highest_found = False
        # determine if a multiplicative match found btw ceiling nums and primes
        for i in range(2,ceiling+1):
            ceiling_found = False
            for j in range(0,len(primes)):
                for k in range(1,len(primes)):
                    if primes[j] * primes[k] == i:
                        ceiling_found = True
                        print "found for " +str(x) + " "+ str(i) + " " + str(j) + " " + str(k)
                        break
            if ceiling_found == True:
                highest_found = True
            else:
                highest_found = False
        if highest_found == True:
            return x
    return None
