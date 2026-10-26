#Q14 WAP to calculate sum of squares of even numbers

num=int(input("Enter a number "))
sum=0

for i in range(1,num+1):
    if i%2==0:
        a= i**2
    
    else:
        a=0
    
    sum+=a

print(sum)