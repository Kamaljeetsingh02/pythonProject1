#
# a = 0
# b = 1
# f = 1
# n = int(input("Till what number would you like to see the fibonacci sequence: "))
# while b <= n:
#     f = a+b
#     a = b
#     b = f
#     print(a)

def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n - 1) + fib(n - 2))

n = int(input("Enter number of terms:"))
print("Fibonacci series:")
for i in range(n):
    print(fib(i))
