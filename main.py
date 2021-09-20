L=["damon","Stefan","Elena","Caroline"]
print(tuple(L))
print(len(L))
print(type(L))
print(L[:4])
print(L[:-1])
L[2]="Claus"
print(L)
L[1:3]="bonnie","alaric","elijah"
print(L)
L.append("Jeremy")
print(L)
L.insert(1,"finn")
print(L)
L1=["1","2","3"]
L.extend(L1)
print(L1)
T=("WE","ARE","best friend")
L.extend(T)
print(L)
L.pop(3)
print(L)
L.remove("3")
L.clear()
print(L)
for i in range(1,10):
  print("The square root is",i**0.5)

for i in range(1, 10,2):
   print("The square root is", i ** 0.5)

x1=int(input("Enter no. 1:"))
x2=int(input("Enter no. 2:"))
count=x1
product=0
while count>0:
    product = product + x2
    count=count-1

print("The product of x1 and x2 is", product)


for i in range(20):
    if i==12:
        continue
    if i==18:
        break
    print(i)
