#Write a menu driven program to accept two strings from the user and perform the various
#functions using user defined functions

def concatenate_strings(str1,str2):
    concatenated_string = str1 + str2
    print("Concatenated string:", concatenated_string)

def find_string_length(string):
    length = len(string)
    print("Length of the string:", length)

def compare_strings(str1, str2):
    if str1 == str2:
        print("Strings are equal.")
    elif str1 < str2:
        print("String 1 is less than String 2.")
    else:
        print("String 1 is greater than String 2.")

def reverse_string(string):
    reversed_string = string[::-1]
    print("Reversed string:", reversed_string)

while True:
    print("\nMenu:")
    print("1. Concatenate strings")
    print("2. Find length of a string")
    print("3. Compare strings")
    print("4. Reverse a string")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        str1 = input("Enter the first string: ")
        str2 = input("Enter the second string: ")
        concatenate_strings(str1,str2)
    elif choice == 2:
        string = input("Enter the string: ")
        find_string_length(string)
    elif choice == 3:
        str1 = input("Enter the first string: ")
        str2 = input("Enter the second string: ")
        compare_strings(str1,str2)
    elif choice == 4:
        string = input("Enter the string: ")
        reverse_string(string)
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")