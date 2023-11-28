#Write a program to print the sum of all the primes between two ranges.

a=int(input("Enter the start range= "))
b=int(input("Enter the end range= "))
sum=0
for i in range(a,b+1):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c=c+1
    if(c==2):
        sum=sum+i

print("Sum of all prime numbers is ",sum)