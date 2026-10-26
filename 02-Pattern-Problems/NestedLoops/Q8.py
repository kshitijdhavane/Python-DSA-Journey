for i in range (1,5):
    print()
    for j in range (1,i+1):
        print(chr(96+j),end="")

    #when i see A,B,C,D,.. use - chr(64+j)
    #when i see 1,2,3,4,.. use - j
    #when i see 0,1,2,3,.. use - count
    #when i see a,b,c,d,.. use - chr(96+j)