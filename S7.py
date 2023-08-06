#find factorie sefareshi abdi ....
while True:
    r =int(input("please enter you number: \n"))
    def factoriel(x):
        n =1
        for i in range (1,r+1 ):
            n = n * i 
        return n
    print  (factoriel(r)) 
    def factoriel2(r):
        if r<=1:
            return 1
        else:
            return r*factoriel2(r-1)
    print (factoriel2(r))
