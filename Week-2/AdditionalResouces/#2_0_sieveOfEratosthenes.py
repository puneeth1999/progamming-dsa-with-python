'''
Implementation of Sieve Of Eratosthenes:
Time Complexity: O(N Log(Log N))
Space Complexity: O(N)
'''
def sieve(n):
	if n <= 1:
		return None 
	from math import sqrt
	numbers = [True for i in range(n+1)]
	primes = []
	numbers[0] = False; numbers[1] = False # Since the numbers 0 and 1 are not considered as Prime.
	for i in range(2, int(sqrt(n+1))+1): # Only need to traverse till the square root of the numbers
		if numbers[i] == True:
			primes.append(i)
			for j in range(i*2, n+1, i): # Marking off the multiples of i
				numbers[j] = False
	# Append the left overs in the list - numbers to primes
	for i in range(i+1, n+1):
		if numbers[i]:
			primes.append(i)
	return primes
print(sieve(25))
print(sieve(36))
print(sieve(41))
print(sieve(0))
print(sieve(98))



