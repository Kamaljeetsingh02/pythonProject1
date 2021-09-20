# def sum(*sum):
# #     return result
# #     for x in num:
# #         result += (x)
# #         sum(1,2)
opt=int(input("plz enter 1 for add,2 for subtract,3 for multiply and 4 for divide"))
a=[]
b=int(input("please en no"))
a.append(int(b))

while b:
    b = input("please en no")
    if b:
        a.append(int(b))
print(a)
def calculator(opt,*args):
    res=0
    for arg in args:
        if(opt==1):
            res +=arg
            return res
calculator()
