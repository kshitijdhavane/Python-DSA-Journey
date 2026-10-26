#   Q4.Write a progrm to enter any character. if entered character is in lowercase then convert it to uppercase and display it. if entered character is in uppercase then convert it to lowercase and display it.

ch = input ('Enter any character: ')
if (ch>='A' and ch<='Z'):
    ch= ch.lower()
    print("The character was in uppercase. In lowercase it is: "+ ch)
else:
    ch= ch.upper()
    print ("The character was in lowercase. In uppercase it is: "+ ch)