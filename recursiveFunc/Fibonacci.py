#print fibnacci sequence

def fibo(num):
	if num <= 1:
		return num
	else:
		return(fibo(num - 1) + fibo(num - 2))
