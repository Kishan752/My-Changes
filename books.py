import math
def pageCount(n, p):
    frontcount=0
    backcount=0
    frontcount+=math.ceil((p-1)/2)
    if n%2!=0 and (n-1) == p:
        backcount=0
    elif n%2!=0:
        backcount+=math.floor((n-p)/2)
    else:
        backcount+=math.ceil((n-p)/2)
    
    return min(frontcount,backcount)
    

        

    


print(pageCount(7,4))