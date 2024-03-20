#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    args = sys.argv
    if len(args) != 4:
        print("Usage: {} <a> <operator> <b>".format(args[0]))
        sys.exit(1)
    
    a, operator, b = int(args[1]), args[2], int(args[3])

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))
