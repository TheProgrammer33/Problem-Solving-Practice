def semi_prime_count(n):
  primes = getPrimes(n)
  semiPrimes = []
  for i in range(len(primes)):
    primeOne = primes[i]
    for primeTwo in primes[i:]:
      product = primeOne * primeTwo
      if (product >= n):
        break
      if not product in semiPrimes:
        semiPrimes.append(product)

  return len(semiPrimes)


def getPrimes(lastNumber):
  primeNumbers = [2]
  for i in range(3, round(lastNumber/2)):
    isPrime = True
    for j in range(2, round(i**(1/2)+1)):
      if (i%j == 0):
        isPrime = False
      if isPrime:
        primeNumbers.append(i)
  return primeNumbers
