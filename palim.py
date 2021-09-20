# def isPalindrome(s):
# 	return s == s[::-1]
# s = ""
# ans = isPalindrome(s)
# if ans:
# 	print("Yes")
# else:
# 	print("No")

num=int(input("Enter the no:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
    if(temp==rev):
        print("The no is palindrome:")
    else:
        print("the no is not palindrome:")
