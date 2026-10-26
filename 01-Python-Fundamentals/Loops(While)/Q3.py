#Q3 WAP to calculate the sum of the numbers from m to n using while loop

m =int(input("Enter the number"))
n =int(input("Enter the number"))
sum=0
while m<=n:
    sum+=m
    m+=1
print("The sum of the numbers from m to n is:",sum)