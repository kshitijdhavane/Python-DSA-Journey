#Q8 WAP taht displays all leap years from 1900- 2101

print("All the leap years from 1900-2101 are: ")
count=0
for i in range (1900,2101,4):
    if i%400==0 or i%4==0 and i%100!=0:
        print(i,end="\t")
        count+=1

print("\n The count of leap year is :", count)
    

