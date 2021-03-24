#!/usr/bin/python3
"""A program that imports all functions from the file calculator_1.py and handles basics operations
"""
if __name__ == "__main__":
    import sys
    import calculator_1 as c
    try:
        op = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        if len(sys.argv) == 4:
            if op == "+":
                print("{:d} + {:d} = {:d}".format(a, b, c.add(a, b)))
            elif op == "-":
                print("{:d} - {:d} = {:d}".format(a, b, c.sub(a, b)))
            elif op == "*":
                print("{:d} * {:d} = {:d}".format(a, b, c.mul(a, b)))
            elif op == "/":
                print("{:d} / {:d} = {:d}".format(a, b, c.div(a, b)))
            else:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
    except IndexError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
