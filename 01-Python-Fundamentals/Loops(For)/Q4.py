#Q4   WAP to calculate the factorial of a number 

n= int(input("Enter a number "))
fact=1         # zero's fact is 1 not 0

for i in range (1,n+1):
    fact=fact*i
print ("The factorial is ",fact)