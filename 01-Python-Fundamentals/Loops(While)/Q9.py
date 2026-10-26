#Q9 WAP to print the reverse of a number 

num= int(input("Enter the number:" ))

while num!=0:
    temp= num%10            # We can also remove the temp 
    print(temp,end="")      #print(num%10,end="")
    num=num//10



   