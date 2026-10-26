#Q5 WAP to read the numbers until -1 is enccountered .find the average of positive numbers, negative numbers and count of zeros using while loop

positives=0
negatives=0
zeros=0
positives_sum=0
negatives_sum=0

while True:
    num =int(input("Enter a -1 to exit: "))
    if num==-1:
        break
    elif num>0:
        positives+=1
        positives_sum+=num
    elif num<0:
        negatives+=1
        negatives_sum+=num
    else:
        zeros+=1
    

if positives>0:
    avg_of_positives = positives_sum/positives
    print("Average of positive numbers:", avg_of_positives)

else:
    print("There is no positive numbers")

if negatives>0:
    avg_of_negatives = negatives_sum/negatives
    print ("Average of negative numbers:", avg_of_negatives)

else:
    print("There is no negative numbers")

if zeros>0:
    print("Count of zeros:", zeros)
else:
    print("There is no zeros")

