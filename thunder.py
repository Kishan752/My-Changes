def jumpingOnClouds(c):
    sum=0
    i=0
    size=len(c)
    while i < (size-1):
        if (i+2) < size and c[i+2] == 0:
            
            sum+=1
            
            i=i+2
        else:
            sum+=1
            
            i=i+1
        
    
    return sum


ar=[0,0,1,0,0,10]
print(jumpingOnClouds(ar))


