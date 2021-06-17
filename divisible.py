def divisibleSumPairs(n, k, ar):
    count=0
    for i in range(len(ar)):
        j=i+1
        while j<len(ar):
            if (ar[i]+ar[j])%k==0:
                count+=1
            j+=1
    
    return count


ar=[1,3,2,6,1,2]
print(divisibleSumPairs(6, 3, ar))
