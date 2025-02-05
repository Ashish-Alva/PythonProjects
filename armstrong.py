num = int(input("Enter a Number: "))
order = len(str(num))
print(f"Order: {order}")
n = 0
sum = 0
copy_num = num
while num>0:
    n = num%10
    sum += n**order
    num = num//10

if copy_num == sum:
    print("It is an Armstrong number")
else:
    print("Not an Armstrong number")