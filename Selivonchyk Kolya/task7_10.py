# Task 7.10
# Implement a generator which will generate odd numbers endlessly.


def endless_generator():
    number = 1
    while True:
        yield number
        number += 2


gen = endless_generator()
while True:
    print(next(gen))