'''
Just added to demostrate the Recursion
'''

# Factorial
def factorial(n):
	if n <= 1:
		return 1
	return n*factorial(n-1)
print(factorial(5))


# Fibanocci
def fibanocci(n):
	if n <= 1:
		return n
	return fibanocci(n-1) + fibanocci(n-2)
print(fibanocci(4))

# Multiply
def multiply(m, n): # Multiply m by n times
	if n==1:
		return m
	return m + multiply(m, n-1)
print(multiply(5,5))


# Length of a list
def lengthOfTheList(l):
	if l == []:
		return 0
	return 1 + lengthOfTheList(l[1:])
print(lengthOfTheList([1, 2, 3, 5]))


# Sum of a list of numbers
def sumOfList(l):
	if l == []:
		return 0
	return l[0]+sumOfList(l[1:])
print(sumOfList([1,2,3,4]))