def  fib(n):
    if(n<=1):
        return n
    return fib(n-1)+fib(n-2)
a=int(input("enter a value:"))
print("no of ways",fib(a+1))
