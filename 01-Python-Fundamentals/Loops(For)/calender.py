startday = int(input("Enter the start day (1-7): "))
num_of_days = int(input("Enter number of days: "))

print("Sun Mon Tue Wed Thu Fri Sat")
print("--------------------------------")

# Print blank spaces before first day
for i in range(startday - 1):
    print("    ", end="")

# Current weekday position
day = startday

# Print dates
for j in range(1, num_of_days + 1):

    print(f"{j:3}", end=" ") #The :3 keeps spacing aligned.

    if day == 7:
        print() #move to the next ROW
        day = 1  #start counting again from sunday
    else:
        day += 1