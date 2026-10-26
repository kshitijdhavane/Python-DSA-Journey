#Q13   WAP to calculate sum of cubes of numbers from 1-n

num=int(input("Enter a number :"))
sum=0

for i in range (1,num+1):
    sum =sum + i**3

print("sum is ",sum)