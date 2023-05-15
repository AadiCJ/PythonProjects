def main():
    in1, op, in2 = input("What is your expression? ").split()
    in1 = float(in1)
    in2 = float(in2)
    if op == "+":
        print(in1 + in2)
    elif op == "-":
        print(in1 - in2)
    elif op == "*":
        print(in1 * in2)
    elif op == "/":
        print(in1 / in2)


main()
