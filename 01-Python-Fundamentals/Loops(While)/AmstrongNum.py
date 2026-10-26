#Q6  WAP to find weather the given number is amstrong or not

num =int(input("Enter a number: "))   #original number (used later for comparison)
s = 0
n = num                               #working copy of the original number (used for calculations)

while n>0:
    r= n%10
    digits= len(str(num))
    s = s + r**digits
    n= n//10          # // (Floor division) - removes the last digit from the number    

if s==num:
    print("The number is an amstrong number.")
else:
    print("The number is not an amstrong number.")