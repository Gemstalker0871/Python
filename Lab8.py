#Make a list of first 10 letters of the alphabet, then use the slicing to do the following
#operations:
#• Print the first 3 letters of the list
#• Print any 3 letters from the middle
#Print the letter from any particular index to the end of the list

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

print("First 3 letters:", alphabet[:3])

middle_start = len(alphabet) // 2 - 1
middle_end = middle_start + 3
print("Middle 3 letters:", alphabet[middle_start:middle_end])

index_to_end = 5
print(f"Letters from index {index_to_end} to the end:", alphabet[index_to_end:])
