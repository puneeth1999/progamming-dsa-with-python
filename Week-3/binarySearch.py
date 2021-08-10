def binarySearch(seq, start, end, target): 
	# seq is the array/list; start and end are the bounds and target is that value to search for
	# Please note that the array -  seq must be in sorted in non-decreasing order for this version of Binary search to work
	if end-start == 0:
		return None
	mid = (start + end) // 2
	if seq[mid] == target:
		return mid
	if target < seq[mid]:
		return binarySearch(seq, start, mid, target)
	else:
		return binarySearch(seq, mid+1, end, target)

print('The element is present in the index:',binarySearch([0,1,2,3,4,5,6,7], 0, 8, 5))