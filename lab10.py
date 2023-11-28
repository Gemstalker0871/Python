#Wap that scans an email address and forms a tuple of name and domain

ed=input("Enter email ")
ap=ed.find('@')
if ap!=-1:


    username=ed[:ap]
    domain=ed[ap+1:]
    print(f"Username : {username}")
    print(f"Domain : {domain}")
else:
    print("Invaild email")