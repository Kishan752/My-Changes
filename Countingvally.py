def countingValleys(steps, path):
    vallycount=0
    isvallystarted=False
    sealevel=0

    for i in path:
        if i == 'U':
            sealevel+=1
           
            if sealevel == 0 and isvallystarted:
                vallycount +=1
        elif i == 'D':
            sealevel-=1
            if sealevel < 0:
                isvallystarted=True

    

    return vallycount   







path=['U','D','D','D','U','D','U','U']
countingValleys(8,path)