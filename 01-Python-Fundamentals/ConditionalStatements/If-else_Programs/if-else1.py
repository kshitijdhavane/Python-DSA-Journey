#   Q1 Write a program to determine whether a person is eligible to vote or not
#   if he not eligible then diplay how many years are left for him to be eligible to vote

age= int(input("Enter your age: "))
if age >=18:
    print("You are eligible to vote.")
else:
    years = 18-age 
    print("You are not eligible to vote. You have to wait for" + str(years) + " years to be eligible to vote.")