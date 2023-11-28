#Wap that reads email id of a person in the form of a string and 
#ensures that it belongs to the domain @gmail.com

str = input("Enter email ")
str1 = "@gmail.com"
str2 = str.count('@')
str3 = str.count('.com')

if str2 == 1 and str3 == 1:
    if str[-10:] == str1:
        print("Correct")
    else:
        print("Incorrect")
else:
    print("Incorrect")