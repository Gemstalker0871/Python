#Write a program to check whether a number is an Armstrong number or not

n = int(input("Enter the number to check Armstrong or not: "))
temp = n
sum = 0
num_digits = 0  # Initialize the count of digits to 0

# Count the number of digits in n
while n > 0:
    num_digits += 1
    n //= 10

n = temp  # Reset n to its original value

while n != 0:
    r = n % 10
    sum += r ** num_digits
    n //= 10

if temp == sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")