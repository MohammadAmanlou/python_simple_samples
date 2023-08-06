while True:
    def reverse_v1(s):
        r = " "
        for char in s:
            r = char + r
        return r
    x = input("give me a string: \n")
    y=reverse_v1(x)
    print (y)
     
    def reverse_v2 (s2):
        rr= ""
        for i in range (len(s2)-1, -1 , -1 ):
            rr = rr +(s2[i])
        return rr
    dd= input("give us a string: \n")
    pp= reverse_v2(dd)
    print (pp)
    
