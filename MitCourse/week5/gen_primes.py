def genPrimes():
    primes = []
    x = 2
    found = 0
    while True:
        for elem in primes:
            if (x % elem) == 0:
                found += 1
        if found == 0:
            primes.append(x)
            found = 0
            yield x
            x += 1
        else:
            x += 1
            found = 0

primeGenerator = genPrimes()
print(primeGenerator.__next__())
print(primeGenerator.__next__())
print(primeGenerator.__next__())
print(primeGenerator.__next__())


