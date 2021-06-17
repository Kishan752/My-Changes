def sockMerchant(n, ar):
    matchedpair={}
    paircount=0

    i=0
    while i< len(ar):
        if not matchedpair.get(i):
            j=i+1
            while j< len(ar):
                if not matchedpair.get(j):
                    if ar[i] == ar[j]:
                        paircount+=1
                        matchedpair[i]=i
                        matchedpair[j]=j
                        break

                j+=1
        
        i+=1
    
    return paircount


ar=[1,2,1,2,1,3,2]
sockMerchant(9,ar)

                
                    


