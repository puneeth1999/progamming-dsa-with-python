exp = '(1+((2+3)*(4*5)))'
def evaluate(s):
	operators = []; operands = []
	for i in range(len(s)):
		if s[i] != ')':
			if s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
				operators.append(s[i])
			elif s[i] == '(':
				continue
			else:
				operands.append(s[i])
		else:
			oper1 = float(operands.pop())
			oper2 = float(operands.pop())
			op = operators.pop()

			if op == '+':
				val = oper1 + oper2
			elif op == '-':
				val = oper1 - oper2
			elif op == '*':
				val = oper1 * oper2
			elif op == '/':
				val = oper1 / oper2
			operands.append(val)
	return operands.pop()
print(evaluate(exp))
