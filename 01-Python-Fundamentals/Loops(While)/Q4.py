negatives= positives =zeros =0

while True   :
    num = int(input("Enter a -1 to exit: "))
    if num==-1:
        break
    elif num>0:
        positives += 1
    elif num<0:
        negatives += 1
    else:
        zeros += 1
print("Positive numbers:", positives)
print("Negative numbers:", negatives)
print("Zeros:", zeros)