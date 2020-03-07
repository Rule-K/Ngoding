def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else :
        fib1 = 0
        fib2 = 1
        for f in range(2,x+1):
            fib3 = fib1 + fib2
            fib1 = fib2
            fib2 = fib3
            return fib3
#Hasil Fibonacci-nya
equal = fibonacci(int(input("Masukan Bilangan: ")))
print(equal)