code = (('i','1'), ('o', '0'),('s','5'),('a','@'),('b','8'))


def passSecure(password):
    for a,b in code:
        password = password.replace(a,b)
        return password

if __name__ == "__main__":
    a = input("Enter a Password: \n")
    password = passSecure(a)
    print(f"Your Secure password is: {password}")