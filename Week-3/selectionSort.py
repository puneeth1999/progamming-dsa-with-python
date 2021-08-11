'''
Notes on SELECTION SORT:
=> Scan the list from left to right
	=> During the scan, perform the following:
	=> Set min_pos to the current position.
	=> Now, scan again using another loop from the current position to the right of the list. Let's call this a slice.
		=> If the present element within the slice is less than min_pos element, l[min_pos] = l[present]
	=> At this point, the minimum value of the current slice is found.
	=> Now, swap the minimum value with the current position
=> Return the list.

Time Complexity	: O(N^2) where N is the size of the input
Space Complexity: O(1) since, it does not take up any extra space
'''

def selectionSort(l):
	# Scans from left to right
	for start in range(len(l)):
		min_pos = start # Gets assigned to the current position of the pointer
		# Starts searching for min value from the current pointer (start) position
		for i in range(start, len(l)):
			if (l[i] < l[min_pos]):
				min_pos = i
		# Swap
		l[min_pos], l[start] = l[start], l[min_pos]
	return l

if __name__ == "__main__":
	print(selectionSort([7,6,4,5,9,2,0,1]))

