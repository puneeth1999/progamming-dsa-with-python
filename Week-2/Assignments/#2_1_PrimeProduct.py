def generatePrimesUptoN(n):
	if n <= 1:
		return False
	
	res = []
	for i in range(2, n+1):
		booler = True
		for j in range(2, i//2 +1):
			if i%j == 0:
				booler = False
		if booler:
			res.append(i)
	return res

def primeproduct(m):
	primes = generatePrimesUptoN(m)
	for i in range(len(primes)):
		for j in range(len(primes)):
			if (primes[i] * primes[j] == m):
				return True
	return False

print(primeproduct(202))