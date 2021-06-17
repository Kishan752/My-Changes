def catAndMouse(x, y, z):
    a= abs(z-x)
    b= abs(z-y)

    if a<b:
        print('Cat A')
    elif a>b:
        print('Cat B')
    else:
        print('Mouse C')



catAndMouse(1,3,2)