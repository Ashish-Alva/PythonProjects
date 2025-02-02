print("Welcome to Restaurent Billing")
print("Enter amount, Press q to exit")
sum = 0
while(True):
    userInput = input("Enter price of the Product: ")
    if(userInput!='q'):

        # Method 1
        # sum += int(userInput)

        # Method 2
        # if userInput.isdigit():
        #     sum += int(userInput)
        # else:
        #     print("Enter a valid number")

        # Method 3
        try:
            val = int(userInput)
            sum += val
        except ValueError:
            print("That's not an int!")


    else:
        print(f"The Total Bill = {sum}, You have exited the Program")
        break