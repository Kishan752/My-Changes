def angryProfessor(k, a):
    arrivalcount=0
    for i in range(len(a)):
        if a[i] <= 0:
            arrivalcount+=1
    
    print(arrivalcount)

    if arrivalcount >= k:
        return "NO"
    else:
        return "YES"


a=[0,-1,2,1,4,5]
print(angryProfessor(4,a))