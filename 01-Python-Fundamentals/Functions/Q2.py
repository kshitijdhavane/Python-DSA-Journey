#WAF to print the multiplication table of a number

def multiplication_table(num):
    for i in range(1, 11):
         a= num*i
         print(num,"x",i,"=",a)
multiplication_table(5)


#WAF to print the square of numbers from 1 to 20.

def square(n):
     
     for i in range (1,n+1):
          print(i**2,end=" ")
square(20)