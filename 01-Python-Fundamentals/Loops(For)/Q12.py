#Q12   WAP to sum a series-- 1/1  +2^2/2 + 3^3/3 +...n^n/n

num=int(input("Enter a number:"))
sum=0

for i in range (1,num+1):
    a= float(i**i)/i
    sum+=a
print (sum)