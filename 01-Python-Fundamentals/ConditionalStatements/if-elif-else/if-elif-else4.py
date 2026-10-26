#Q4    Write a program that a user enter a number bet 1-7 and display the name of the day of the week 

num=int(input("Enter a number between 1 and 7: "))
if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3:
    print("Wednesday")
elif num==4:
    print("Thursday")
elif num==5:
    print("Friday")
elif num==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("Wrong input")