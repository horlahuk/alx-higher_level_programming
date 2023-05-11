#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    plus = add(a, b)
    minus = sub(a, b)
    multiply = mul(a, b)
    divide = div(a, b)
    print("{:d} + {:d} = {:d}\n{:d} + {:d} = {:d}\n{:d} + {:d} = {:d}\n{:d} + {:d} = {:d}".format(a, b, plus, a, b, minus, a, b, multiply, a, b, divide))
