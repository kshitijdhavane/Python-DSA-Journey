#Q1 WAP to calculate average of first n natural numbers

n=int(input("Enter the Number "))
sum=0
for i in range(1,n+1):
    sum+=i
    print(i,end="\t")
avg =sum/n

print("\nThe sum ",sum)
print("The avg ",avg)
