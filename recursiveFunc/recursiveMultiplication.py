#multiply recursively
def prod(num1, num2):
	if num1 < num2:
		return prod(num2, num1)
	elif num2 != 0:
		return (a + prod(num1, num2))
	else:
		return 0