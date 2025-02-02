import string
import random

if __name__ == '__main__':
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation
    # print(s1,s2,s3)
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    # random.shuffle(s)
    # print(s)
    len = int(input("Enter length of Password : "))
    print("Your password is: ")
    # print("".join(s[0:len]))

    print("".join(random.sample(s,len)))