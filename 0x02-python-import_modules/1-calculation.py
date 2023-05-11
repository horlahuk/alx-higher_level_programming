#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    plus = add(a, b)
    minus = sub(a, b)
    multiply = mul(a, b)
    divide = div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, plus))
    print("{:d} + {:d} = {:d}".format(a, b, minus))
    print("{:d} + {:d} = {:d}".format(a, b, multiply))
    print("{:d} + {:d} = {:d}".format(a, b, divide))
