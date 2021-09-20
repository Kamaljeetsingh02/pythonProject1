for i in range(0,4):
    for j in range(0,i-4):
        print(" ",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    print("*")

    num1 = int(input("Enter the no"))
    num2 = int(input("Enter the no"))
    sum = 0


    def add():

        sum = num1 + num2


    print(f'the sum of {num1} and {num2} is {sum}')
