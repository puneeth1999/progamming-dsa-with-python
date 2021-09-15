def Merge(A, B):
	(C, m, n) = ([], len(A), len(B))
	i = j = 0
	while(i+j < m+n): # i+j tells us how many elements have been merged so far
		# Base Case: if A is empty and B is not yet empty
		if i >= m:
			C.append(B[j])
			j += 1
		# Base Case: if B is empty and A is not yet empty
		elif j >= n:
			C.append(A[i])
			i += 1
		# Comparisons
		elif A[i] <= B[j]: # The use of "<=" instead of "<" ensures stable sorting
			C.append(A[i])
			i += 1
		else:
			C.append(B[j])
			j += 1
	return C

def MergeSort(A, l, r):
	if r-l <= 1:
		return A[l:r]
	mid = (r+l)//2
	L = MergeSort(A, l, mid)
	R = MergeSort(A, mid, r)
	return Merge(L, R)

# A = [3,4,1,4,68,32,0,2]
# print(MergeSort(A, 0, len(A)))