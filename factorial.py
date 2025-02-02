def factorial(num):
    if num == 0 or num == 1:
        return 1
    else: 
        return num * factorial(num-1)

def factorialTrailingZeros(num):
    count = 0
    i = 5
    while(num//i != 0):
        count += int(num/i)
        i = i*5
    return count

if __name__ == "__main__":
    num = int(input("Enter a Number: "))
    fact = factorial(num)
    print(f"Factorial is: {fact}")
    tfact = factorialTrailingZeros(num)
    print(f"Factorial Trailing zero is: {tfact}")