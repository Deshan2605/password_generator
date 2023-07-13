import random

char1 = "abcdefghijklmnopqrstuvwxyz"
char2 = "0123456789"
char3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
char4 = "!@#$%^&*()"
char5 = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"

length = int(input("Enter the length of your password: "))
password = ""

password += random.choice(char1)  # Ensure the first character is a random lowercase letter
password += random.choice(char2)
password += random.choice(char3)
password += random.choice(char4)

for _ in range(length - 4):
    password += random.choice(char5)

password_list = list(password)
random.shuffle(password_list)
shuffled_password = ''.join(password_list)

print("Your password is:", shuffled_password)
