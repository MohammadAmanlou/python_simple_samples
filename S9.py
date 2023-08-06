def fibo(x):
        if x==0:
            return 0
        elif x==1:
            return 1
        else :
            return fibo(x-1)+fibo(x-2)
while True:
    x = int(input("fibo ta chand? \n"))
    for i in range (0,x):
        print (fibo(i))
        
        
