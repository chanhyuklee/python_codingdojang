def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))
