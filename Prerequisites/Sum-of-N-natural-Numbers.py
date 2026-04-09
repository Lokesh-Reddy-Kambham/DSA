num = int(input("Enter Number:"))
def total(number):
    s = 0
    for i in range(1,number+1):
        s += i
    return s
print(total(num))

print(sum(range(num+1)))
