import random
print("**Welcome to OTP Generator**")
digit=int(input("Enter the number of digits that you want OTP-:"))
#OTP IS NOT GREATER THAN 6 DIGIT #
x=random.random()
rev=int(str(x)[::-1][0:digit])
print(rev)