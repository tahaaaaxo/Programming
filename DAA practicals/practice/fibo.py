def fibo_rec(n):
    if n <= 1:
        return n
    return fibo_rec(n-1)+fibo_rec(n-2)


print(fibo_rec(5))
