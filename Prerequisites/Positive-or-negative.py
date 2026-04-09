num = int(input())
def positive_negative(number):
    if number > 0:
        print("positive")
    elif number < 0:
        print("negative")
    else:
        print("neutral")
print(positive_negative(num))
print("Postive" if num >0 else "Negative")