def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
sum = 0
i = 2
while(True):
    res = fib(i)
    i += 1
    print(res)
    if res>4_000_000:
        break
    sum += res * (1-res%2)
print(sum)
