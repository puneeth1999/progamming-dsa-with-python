# Expanding
def expanding(l):
	if len(l) <= 2:
		return True # If there are only 2 or less than 2 elements, the condition already satisfies.
	main_diff = max(l[1], l[0]) - min(l[1], l[0])
	for pos in range(1, len(l) - 1):
		curr_diff = max(l[pos], l[pos+1]) - min(l[pos], l[pos+1])
		if curr_diff <= main_diff:
			return False
		else:
			main_diff = curr_diff
	return True
print(expanding([1,3,7,2,9]))
print(expanding([1,3,7,2,-3]))
print(expanding([1,3,7,10]))
print(expanding([1]))
print(expanding([1,-1]))
print(expanding([1,2,2]))




# Sum Square
def sumsquare(l):
	even_sqr = 0; odd_sqr = 0;
	for element in l:
		sqr = element*element
		if element % 2 == 0:
			even_sqr += sqr
		else:
			odd_sqr += sqr
	return [odd_sqr, even_sqr]

print(sumsquare([1,3,5])) 		# Expected Output: [35, 0]
print(sumsquare([2,4,6])) 		# Expected Output: [0, 56]
print(sumsquare([-1,-2,3,7])) 	# Expected Output: [59, 4]

