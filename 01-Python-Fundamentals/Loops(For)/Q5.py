#Q5 WAP to classify the given number is prime or composite

n= int(input("Enter a number "))
count=0
for i in range (1,n+1):
    if n%i==0:
        count=count+1

if count==2:
    print("The number is prime ")

else:
    print("Composite number")
