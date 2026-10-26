#Q7 WAP to calculate pow(x,n)

num= int(input("Enter a number : "))
n= int(input("Till which power to calculate "))

result=1

for i in range (n):
    result=result*num

print(num,"raised to power",n,"is",result)

