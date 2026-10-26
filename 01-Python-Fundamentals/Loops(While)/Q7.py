#Q7 WAP to enter a number then calculate the sum of its digits

num= int(input("Enter a number "))
sum= 0
n = num
while(n!=0):
     n = num%10
     sum= sum+n
     num=num//10

print("The sum of the digits of the number is: ", sum)