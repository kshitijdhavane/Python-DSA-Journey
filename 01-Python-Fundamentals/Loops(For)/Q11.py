#Q11   WAP to sum series-- 1/2+2/3+...n/(n+1)

num=int(input("Enter a number "))
sum=0

for i in range (1,num+1):
    a=float(i)/(i+1)
    sum+=a
print("the sum is ",sum)
