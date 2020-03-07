def fibonacci(x):
	if x == 0:
		return 0
	elif x == 1:
	    return 1
    else :
        fiba = 0 
    	fibb = 1
    	for i in range(2,x+1):
    		fib = fiba + fibb
    		fiba = fibb
    		fibb = fib
    		return fib

hasil = fibonacci(10)
print(hasil)