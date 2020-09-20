# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Random Password Generator

# +
import random
import string

print(string.printable[0:10])
print(string.printable[10:36])
print(string.printable[36:62])
print(string.printable[62:94])


numPass = 3
passwordd = ''
for n in range(numPass):
    u = random.randint(0, 10)
    passwordd += string.printable[u]
print(passwordd)

litllPass = 5
passworddd = ''
for n in range(litllPass):
    u = random.randint(11, 36)
    passworddd += string.printable[u]
print(passworddd)


# def start():
#     def generate_pass(num):
#         password = ''
#         for n in range(num):
#             x = random.randint(0, 93)
#             password += string.printable[x]
#
#         return password
#
#     try:
#         num = int(input("Enter the number of characters: "))
#         print(generate_pass(num))
#         start()
#     except ValueError:
#         print("REMEMBER TO ENTER AN INTEGER.\n")
#         start()
#
#
# start()
# -

# ##### 17

a = int(input("Enter a number: "))
if abs(1000 - a) <= 100 and a <= 1100:
    print("This number is within a hundred of 1000.")
elif abs(2000 - a) <= 100 and a <= 2100 :
    print("This number is within a hundred of 2000.")
else:
    print("This number is not within a hundred of 1000 or 2000.")

# ##### 18

a = 1 
b = 3
c = 1
if a == b == c:
    print(3*(a + b + c))
else:
    print(a + b + c)

# ##### 19

s = "IsEmpty"
if len(s) >= 2 and s[:2] == "Is":
    print(s)
else:
    print("Is" + s)

# ##### 20

s = "Pipiripi"
r = ""
n = 3
for i in range(n):
    r = r + s
print(r)

# ##### 21

n = int(input("Enter a number: "))
if n%2 == 0:
    print("It is an even number!")
else:
    print("It is an odd number!")

# ##### 22


