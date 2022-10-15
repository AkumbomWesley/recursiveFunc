#To the power of
def power(base, exp):
	if(exp == 1):
		return (base)
	elif(exp != base):
		return (base * power(base, exp - 1))