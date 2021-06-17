def bonAppetit(bill, k, b):
    i=0
    sum=0
    while i< len(bill):
        if i!=k:
            sum+=bill[i]
        i+=1
    
    if (sum/2) == b:
        print('Bon Appetit')
    else:
        print(int(b-((sum/2))))


ar=[3,10,2,9]
bonAppetit(ar,1,12)

    