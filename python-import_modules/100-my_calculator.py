#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    if len(sys.argv) == 4:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{}".format(calculator_1.add(num1,num2)))
        elif sys.argv[2] == "-":
            print("{}".format(calculator_1.sub(num1,num2)))
        elif sys.argv[2] == "*":
            print("{}".format(calculator_1.mul(num1,num2)))
        elif sys.argv[2] == "/":
            print("{}".format(calculator_1.div(num1,num2)))
    else:
        print("{}".format(1))
