import calculator
for i in range(2):
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter first number: "))

    calculatorObj = calculator.Calculator(number1,number2)

    print(f" ------------- Operation is : {calculator.Calculator.op_count} --------------")
    add = calculatorObj.add()
    print("Addition is",add)

    print(f" ------------- Operation is : {calculator.Calculator.op_count} --------------")
    sub = calculatorObj.sub()
    print("Sub is",sub)

    print(f" ------------- Operation is : {calculator.Calculator.op_count} --------------")
    divide = calculatorObj.divide()
    print("Division is :", divide)

    print(f" ------------- Operation is : {calculator.Calculator.op_count} --------------")
    mult = calculatorObj.multi()
    print("Multiplication is", mult)

