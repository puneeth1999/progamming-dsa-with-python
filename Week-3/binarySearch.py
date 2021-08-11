'''
Notes on BINARY SEARCH:

=> Check if the middle element of the current array is the element you're searching for. If yes, return.
=> Else, there are two scenarios.
	1. The target element is greater than the middle element.
	2. The target element is lesser than the middle element.
=> Scenario 1 [target > middle]:
	=> Return the function with modified parameters. Let it only search the slice from middle+1 till end
=> Scenario 2 [target < middle]:
	=> Return the function with modified parameters. Let it only search the slice from the start to middle.

=> Here, we can see that the slices are cut into half everytime we fail to find the element i.e., every iteration.
   So...

   Time Complexity  = O(log N)
   Space Complexity = O(1) Since we aren't using any additional space.
'''

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