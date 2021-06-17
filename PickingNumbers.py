def pickingNumbers(a):
    currentArray=[]
    i=0
    while i < len(a):
        tempArray=[a[i]]
        j=0
        while j< len(a):
            if i!=j and (a[i]-a[j] == 1 or a[i]-a[j]==0):
                tempArray.append(a[j])
            j+=1
        if len(tempArray) > len(currentArray):
            currentArray=tempArray
        i+=1
    
    print(currentArray)


ar=[1,2,2,3,1,2]
pickingNumbers(ar)
        
      