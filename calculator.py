print("*****smaple calculator*****".center(70))
n=int(input("Enter a number:"))
if n>5:
    print("Please enter a number 1 to 5")
else:
    pass
if n==5:
    print("Exit")
else:
    n1=int(input("Enter n1:"))
    n2=int(input("Enter n2:"))
    if n==1:
        def add(n1,n2):
            return n1+n2
        print(add(n1,n2))
    elif n==2:
        def subtraction(n1,n2):
            return n1-n2
        print(subtraction(n1,n2))
    elif n==3:
        def multiplication(n1,n2):
            return n1*n2
        print(multiplication(n1,n2))
    elif n==4:
        def division(n1,n2):
            return n1/n2
        if n2==0 :
            print("enter valid number:")
            n2=int(input("Enter n2:"))
        print(division(n1,n2))
    else:
        pass
    
        

