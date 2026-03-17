num = int(input("Enter Number:"))
power = 0
while 2**power<=num:
    power+=1
power -= 1
print(2**power)
result = " "
remainder = 0
for i in range(power,0,-1):
    if num%(2**power)<=0:
        result += str(1)
        num = num%(2**power)
        print(num%(2**power))
        print(remainder)
    else:
        result += str(0)
        num = num%(2**power)
print(result)