while True:
    def jam_zarb(x , y):
        jam= x + y
        zarb = x * y
        return (jam , zarb)
    x = int (input("first num: "))
    y = int (input("second num: "))
    (j , z) =(jam_zarb(x,y))
    print ("jam is :" , j , "zarb is :" , z)
