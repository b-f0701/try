def BinarySearch(l,key):
    low = 0;
    high = len(k)-1
    i = 0
    while(low <= high):
        i = i+1
        mid = (high + low)//2
        if (k[mid] < key):
            low = mid + 1
        elif (k[mid] > key):
            high = mid -1
        else:
            print('use %d times' % i)
            return mid

    return -1


k = [1,5,6,9,10,51,62,65,70]
print(BinarySearch(k,70))
print(BinarySearch(k,10))
