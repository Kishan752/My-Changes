def breakingRecords(scores):
    bestscore=scores[0]
    leastScore=scores[0]
    bestcount=0
    leastcount=0
    


    for sc in range(len(scores)):
        print(scores[sc])
        
        if scores[sc] > bestscore:
            bestcount+=1
            bestscore=scores[sc]
        elif scores[sc] < leastScore:
            leastcount+=1
            leastScore=scores[sc]
    
    
    returnArray=[bestcount,leastcount]
    return returnArray

scores=[10,5,20,20,4,5,2,25,1]
print(breakingRecords(scores))


