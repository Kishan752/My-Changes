def birthday(s, d, m):
    count=0
    for sc in range(len(s)-(m-1)):
        sum=0
        for i in range(m):
            sum+=s[sc+i]
        if(sum==d):
            count+=1

    return count


s=[1,1,1,1,1,1]
print(birthday(s,3,2))