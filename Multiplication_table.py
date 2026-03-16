# Multiplication Table using function

def table(num):
    print(f"Table of {num}is..")
    for index in range(1,11):
        print(f"{num} x {index} = {num * index}")

number = int(input("Enter a Number:"))
table(number)
