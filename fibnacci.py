def Fibnacci():
    x , y = 0,1
    print(x)
    print(y)
    sum = 0
    while (sum<100):
        sum = x + y
        print(sum)
        x = y
        y = sum
        
Fibnacci()

