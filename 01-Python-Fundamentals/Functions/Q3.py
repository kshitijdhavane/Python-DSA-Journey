def count_positive(arr):
    count =0

    for num in arr:
        if num > 0:
            count = count+1


    return count 

print(count_positive([3, -2, 5, 0, -1, 7]))