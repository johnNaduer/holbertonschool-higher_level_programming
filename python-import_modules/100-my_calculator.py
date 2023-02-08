#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    if len(sys.argv) == 4:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[3])

        if sys.argv[2] == "+":
            print("{} + {} = {}".format(num1, num2, calculator_1.add(num1, num2)))
        elif sys.argv[2] == "-":
            print("{} - {} = {}".format(num1, num2, calculator_1.sub(num1, num2)))
        elif sys.argv[2] == "*":
            print("{} * {} = {}".format(num1, num2, calculator_1.mul(num1, num2)))
        elif sys.argv[2] == "/":
            if num2 == 0:
                exit(1)
            else:
                print("{} / {} = {}".format(num1, num2, calculator_1.div(num1, num2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
