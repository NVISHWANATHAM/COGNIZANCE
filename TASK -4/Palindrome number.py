print("Enter a Number \n")
num = int(input())
rev = 0

#Copying the original number
temp = num

#Finding Reverse
while temp > 0:
    rev = (rev*10) + (temp %10);
    temp = temp//10

#Comparing reverse with original number
if rev == num :
    print("Palindrome \n")
else:
    print("Not Palindrome")