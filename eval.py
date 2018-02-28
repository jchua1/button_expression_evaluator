import sys

def evaluate():
	exp = raw_input("Enter an expression:\n")
	exp = exp.split(" ") # Assuming all tokens are separated by one white space

	# stacks to contain the operators and numbers of the latest expression to be evaluated
	op_stack = []
	num_stack = []

	for i in exp:
		if i == "+" or i == "-":
			op_stack.append(i)
		else:
			num_stack.append(int(i))

	while num_stack:
		# evaluates addition/subtraction of two numbers
		if op_stack:
			operator = op_stack.pop()
			num2 = num_stack.pop()
			num1 = num_stack.pop()

			if operator == "+":
				answer = num1 + num2
			else:
				answer = num1 - num2

			num_stack.append(answer)
		# evaluates single numbers 
		else:
			answer = num_stack.pop()
			print "Answer: " + str(answer)

evaluate()