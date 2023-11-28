#Write a program to find smallest and largest number in a list

max = 0
min = 0
list=[]

n=int(input("Enter list limit "))
for i in range (0 ,n):
    element = int(input("Enter element "))
    list.append(element)

max = min = list[0]

for i in list:
    if max <= i:
        max = i
    elif min >= i:
        min = i

print("Largest number is " , max)
print("Smallest number is " , min)