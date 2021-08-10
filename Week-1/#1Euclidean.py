def gcd(m,n):
	if m < n:
		m,n = n,m
	while n:
		m, n = n, m%n
	return m
print(gcd(12,24))