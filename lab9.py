#wap that displays options for inserting or 
#deleting elements in a list. if a user chooses 
#a deletion option display a sub menu and ask 
#if element is to be deleted with value or by using 
#its position

number = []
n = int(input("Enter the range: "))

for i in range(1, n + 1):
    ele = int(input("Enter element: "))
    number.append(ele)

# Calculate the sum of elements ending with 7
sum_ending_with_7 = 0
for j in number:
    if j % 10 == 7:
        sum_ending_with_7 += j

print("Sum of elements ending with 7 is:", sum_ending_with_7)