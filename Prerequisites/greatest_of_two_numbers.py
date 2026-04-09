def greatest(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        return f"{number1} is Greatest Number"
    elif number2 > number1 and number2 > number3:
        return f"{number2} is Greatest Number"
    elif number3 > number1 and number3 > number2:
        return f"{number2} is Greatest Number"
    elif number1 == number2 and number2 > number3:
        return f"{number2} is Greatest Number"
    elif number2 == number3 and number3 > number1:
        return f"{number3} is Greatest Number"
    else :
        return f"{number1} is Greatest Number"
    return f"All are Equal"

num1 = int(input("Enter Number:"))
num2 = int(input("Enter Number:"))
num3 = int(input("Enter Number:"))

print(greatest(num1, num2 , num3))