'''
For proper visualization of how the following algorithm works, check out the link below:
https://www.youtube.com/watch?v=wObxd4Kx8sE

Time Complexity:  O(N^2)
Space Complexity: O(1)
'''

def insertionRecurse(l, n):
	if n > 1:
		insertionRecurse(l, n-1)
		insert(l, n-1)
	return l

def insert(l, n):
	pos = n
	while pos > 0 and l[pos] < l[pos - 1]:
		l[pos], l[pos - 1] = l[pos - 1], l[pos]
		pos -= 1

print(insertionRecurse([9, 6, 8, 7, 3, 5, 4, 2, 1], len([9, 6, 8, 7, 3, 5, 4, 2, 1])))