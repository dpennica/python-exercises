#!/usr/bin/python


def fib(n):
    sequence = []
    a, b = 0, 1
    while a < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence


if __name__ == '__main__':
    print(fib(30))
