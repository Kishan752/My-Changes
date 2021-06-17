def hurdleRace(k, height):
    maxnum=0
    for i in height:
        if i>maxnum:
            maxnum=i
    
    if maxnum > k:
        return maxnum - k
    else:
        return 0

ar=[2,5,4,5,2]
print(hurdleRace(7,ar))
        
