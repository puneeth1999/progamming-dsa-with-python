'''
Notes on INSERTION SORT:

The code is pretty self-explanatory

Time Complexity  = O(N^2)
Space Complexity = O(1)
'''

def insertionSort(l):
	for pointer in range(len(l)):
		pos = pointer
		while (pos > 0 and l[pos] < l[pos - 1]):
			l[pos], l[pos - 1] = l[pos - 1], l[pos]
			pos -= 1
	return l
if __name__ == "__main__":
	print(insertionSort([7,6,4,5,9,2,0,1]))