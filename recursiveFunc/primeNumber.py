#prime number:
def primeNumber(num, x = 2):
	if num == x:
		return True
	elif num % x == 0:
		return False
	return primeNumber(num, x+1)