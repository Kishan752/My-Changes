def reverseArray(a):
    i=len(a)-1
    revAr=[]
    while i >= 0:
        revAr.append(a[i])
        i-=1
    
    return revAr



ar=[0,0,1,0,0,10]
reverseArray(ar)

    