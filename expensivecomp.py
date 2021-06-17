def getMoneySpent(keyboards, drives, b):
    maxcost=-1

    for i in keyboards:
        for j in drives:
            if (i+j) <= b and (i+j) > maxcost:
                maxcost=i+j

    
    return maxcost



kayboard=[3,1]
drives=[5,2,8]

print(getMoneySpent(kayboard,drives,10))

