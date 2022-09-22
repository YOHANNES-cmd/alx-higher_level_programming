#!/usr/bin/python3

if __name__ == "__main__":
    """a program that imports all functions from the
    file calculator_1.py and handles basic operations."""

    from calculator_1 import add, sub, mul, div
    import sys

    args = sys.argv
    operators = ['+', '-', '*', '/']

    if len(args) == 4:
        a = int(args[1])
        op = args[2]
        b = int(args[3])

        if op not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            if op == '+':
                print(f"{a} {op} {b} = {add(a, b)}")
            elif op == '-':
                print(f"{a} {op} {b} = {sub(a, b)}")
            elif op == '*':
                print(f"{a} {op} {b} = {mul(a, b)}")
            else:
                print(f"{a} {op} {b} = {div(a, b)}")
            sys.exit(0)
    else:
        print(f"Usage: {args[0]} <a> <operator> <b>")
        sys.exit(1)
