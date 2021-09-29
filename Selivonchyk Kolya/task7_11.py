# Task 7.11
# Implement a generator which will geterate [Fibonacci numbers]


def endless_fib_generator():
    x1 = 1
    x2 = 1
    while True:
        yield x1
        x1, x2 = x2, x1 + x2


gen = endless_fib_generator()
while True:
    print(next(gen))
