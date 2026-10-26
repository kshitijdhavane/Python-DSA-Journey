#Q10   WAP to sum series - 1/1^2+ 1/2^2+....1/n^2

num =int(input("Enter a number "))
sum=0.0

for i in range (1,num+1):
    a= 1/i**2
    sum+=a
print("SUM is ", sum)