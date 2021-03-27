import termcolor2
number = int(input("Enter Number: "))

n = len(str(number))

print(f"Number Of Digits: {n}")
sum = 0
num = number

while num > 0:
    digit = num % 10
    sum = sum + digit ** n
    num //= 10

if sum == number:
    print(termcolor2.colored("yes" ,color="green"))
else:
    print(termcolor2.colored("No" ,color="red"))
