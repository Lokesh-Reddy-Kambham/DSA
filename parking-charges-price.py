try:
    num = int(input("Enter a number:" ))
    if num < 0:
        print("Error: Invalid hours")
    else:
        if num <= 2:
            print(f"Price is {num * 100}")
        elif 2 < num <= 5:
            print(f"Price is {200 + (num - 2) * 50}")
        else:
            print(f"Price is {350 + (num - 5) * 20}")
except ValueError:
    print("Error: Invalid Input")
