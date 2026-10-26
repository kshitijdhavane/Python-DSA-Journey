#Q3  WAP to print all the numbers from m-n therebyclassify them as even or odd 

m= int(input("Enter m"))
n=int(input("Enter n"))

for i in range(m,n+1):
    if i%2==0:
        print(i,"Even number")

    else:
        print(i,"Odd number ")
