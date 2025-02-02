with open('currencyDatabase.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split('\t')
    currencyDict[parsed[0]] = parsed[1]
    

amount = int(input("Enter the amount:\n"))

print("Enter currency to convert into, Available options are\n")
[print(item) for item in currencyDict.keys()]
currency = input("Enter the option: \n")
print(f'{amount} in INR is equal to {round(amount* float(currencyDict[currency]))} {currency}')