def fibonacci(limt):
    a,b = 0, 1
    while a< limt:
        yield a
        a,b = b , a+b



for num in fibonacci(10):
    print(num)