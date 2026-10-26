#Q6  WAP using while loop to read the number until -1 is encountered , aslo, count the numbers of prime number and composite numbers entered by user 

prime_total= 0
composite_total=0

while True:
    n=int(input("Enter a number"))
    if n==-1:
        break
    is_composite=0

    for i in range (2,n):
        if n%i==0:
            is_composite=1
            break

    if (is_composite):
        composite_total+=1
    else:
        prime_total+=1

print("Total composite ",composite_total)
print("Total prime ",prime_total)



