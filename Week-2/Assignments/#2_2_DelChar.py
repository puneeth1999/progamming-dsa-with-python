def delchar(s,c):
	if len(c) > 1:
		return s
	new_s = ""
	for x in s:
		if x == c:
			continue
		new_s += x
	return new_s
# Test Cases
print(delchar("banana", "b"))
print(delchar("banana","a"))
print(delchar("banana","n"))
print(delchar("banana","an"))