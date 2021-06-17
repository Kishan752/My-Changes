def migratoryBirds(arr):
    ar=[0,0,0,0,0,0]

    for i in range(len(arr)):
        ar[arr[i]]+=1
    

    maxcount=0
    for j in range(len(ar)):
        if ar[j]>ar[maxcount]:
            maxcount=j
        
    return maxcount

    



ar=[1,1,1,2,1,3]
migratoryBirds(ar)
