import random
chars="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
length=int(input("Enter the length of your password: "))
password=""

for a in range(length):
    password+=random.choice(chars)

print("Your password is:",password)