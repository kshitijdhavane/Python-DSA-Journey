#Q8 WAP to calculate GCD of two numbers using while loop

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))


while num2!=0:          # This is Euclidean algorithm to find GCD of two numbers
    rem = num1%num2     # Find remainder 
    num1= num2          # Shift the number because we no longer need the first number
    num2 = rem          #Store the remainder


print("The GCD is  ",num1)


# if the num2> num1 - its completely ok because the numbers are eventually going to get swapped 