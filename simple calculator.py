num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
oper = input("Enter the operator (+, -, *, /, %) : ")

match oper:
    case "+":
        add = num1 + num2
        print(f"The sum of the two numbers is {add}")

    case "-":
        subtract = num1 - num2
        print(f"The difference of the two numbers is {subtract}")

    case "*":
        product = num1 * num2
        print(f"The product of the two numbers is {product}")

    case "/":
        quotient = num1 / num2
        print(f"The quotient of the two numbers is {quotient}")

    case "%":
        modulus = num1 % num2
        print(f"The remainder of the division of the two numbers is {modulus}")

