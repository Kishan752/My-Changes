#hacker Rank problem on UtopianTree  
def utopianTree(n):
    height=1
    i=1
    while i <= n:
        if(i%2==0):
            height+=1
        else:
            height*=2
        i+=1
        
    
    return height

print(utopianTree(1))


