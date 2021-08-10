def shuffle(l1, l2):
	# Base Case - 1 => If both are empty lists
	if len(l1) == 0 and len(l2) == 0:
		return []
	# Base Case - 2 => One of the lists is empty
	elif len(l1) == 0 and len(l2) != 0:
		return l2
	# Base Case - 2 => One of the lists is empty
	elif len(l1) != 0 and len(l2) == 0:
		return l1 
	new_list = []
	for i in range(min(len(l1), len(l2))):
		new_list.append(l1[i])
		new_list.append(l2[i])
	if len(l1) > len(l2):
		for i in range(i+1, len(l1)):
			new_list.append(l1[i])
	else:
		for i in range(i+1, len(l2)):
			new_list.append(l2[i])
	return new_list

# Test Cases
print(shuffle([0,2,4],[1,3,5]))
print(shuffle([0,2,4],[1]))
print(shuffle([0],[1,3,5]))
print(shuffle([], []))
print(shuffle([], [0]))
print(shuffle([1,2], []))
