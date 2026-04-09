num = int(input("Enter Number:"))
def even_or_odd(number):
    if number % 2 == 0:
        return "EVEN"
    else:
        return "ODD"
print(even_or_odd(num))
print("EVEN" if num % 2 == 0 else "ODD")
