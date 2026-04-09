def sum_of_numbers(number1, number2):
    total = 0
    for i in range(number1, number2+1):
        total += i
    return total
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
print(sum_of_numbers(num1, num2))

print(sum(range(num1,num2+1)))