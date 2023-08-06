#fibonachi
while True:
    n = int(input("jam 1 ta chand? \n"))
    
    def fib(x):
        sum = 0
        for i in range (1,n+1):
            sum= sum +i
        return sum
    x = fib(n)
    y= fib(x)
    print (y)

