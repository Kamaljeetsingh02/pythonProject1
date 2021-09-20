a: int=int(input("Enter the digit: "))
if a<0 or a>999:
    print("invalid no")
else:
    if a<10:
        print(a,"is one digit no")
    elif a<100:
        print(a,"is two digit no")
    else:
        print(a,"three digit no")




def(a,b):
num=int(input("Enter the no:"))
if (num % 2)==0:
    print("no is even")
else:
    print("no is odd")