def QuickSort(A, left, right):
	if (right-left <= 1):
		return A[left:right]
	yellow = green = left + 1
	for green in range(left, right):
		if A[green] < A[left]:
			A[green], A[yellow] = A[yellow], A[green]
			yellow += 1
	A[left], A[yellow-1] = A[yellow-1], A[left]
	QuickSort(A, left, yellow)
	QuickSort(A, yellow, right)
	return A
A = [85, 5, 2, 0, -5, 56]
print(QuickSort(A, 0, len(A)))
