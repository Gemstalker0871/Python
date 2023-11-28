#wap that displays options for inserting or deleting elements 
#in a list. if the user chooses a deletion operation, display 
#a sub-menu and ask if element is to be deleted with value or 
#by using its position.

while True:
    print("Menu")
    print("1-Insert Element")
    print("2-Delete Element")
    print("3-Exit")

    lst=[1,2,3,4,5]

    choice = input("Enter Choice ")

    if choice == '1':
        m = int(input("Insert Elemnt "))
        lst.append(m)
        print("List ", lst)
    elif choice == '2':
        print("a-By value")
        print("b-By value")
        ch = input("Enter Choice ")

        if ch == 'a':
            num = int(input("Enter Value "))
            lst.remove(num)
            print("After Deletion ", lst)
        elif ch== 'b':
            num = int(input("Enter Index "))
            lst.pop(num)
            print("After Deletion", lst)
        else:
            print("Wrong Choice")

    elif choice == '3':
        break

    else:
        print("Wrong")