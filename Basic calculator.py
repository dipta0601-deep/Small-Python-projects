
print("Calculator")

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print("Enter Operation: '+' for addition,\n '-' for subtraction,\n '*' for multiplication,\n '/' for Division")

operators = ["+", "-", "*", "/"]
operation = input(f"Enter operation between {operators} : ")
n = 5
def Calculator():
    for Calculator in range(1,n+1):
        if operation == "+":
            return n1 + n2
        elif operation == "-":
            return n1 - n2
        elif operation == "*":
            return n1*n2
        elif operation == "/":
            return n1/n2

a = Calculator()
print("You have choosen: ", operation)
print("The answer is: ", a)