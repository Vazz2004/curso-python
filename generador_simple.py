def my_generador():
    yield 1
    yield 2
    yield 3


for values in my_generador():
    print(values)