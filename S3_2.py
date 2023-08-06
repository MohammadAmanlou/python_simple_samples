import time
t=time.time()
a=1
#show if the number is prime or not and list the prime number from 1 to x
while a==1:
    r=0
    this_number= 1
    x = int(input("enter the number: "))
    if (x ==1 or x==0):
        print ("not prime")
    elif x==2:
        print("prime")
    else:
        while(this_number<x**0.5):
            this_number=this_number+1
            if(x%this_number==0):
                r=1
                print ("not prime")
                break
        if (r==0):
            print("prime")
    a=0
    t2=time.time()
    print(t2-t)
    #this_numberr=2
    #while (this_numberr<x+1):
        #is_prime_number = True
        #counter=2
        #while (counter< (this_numberr-1)):
            #if (((this_numberr) % counter)==0):
                #is_prime_number = False
                #break
            #counter= counter +1
        #if (is_prime_number== True):
            #print (this_numberr)
        #this_numberr= this_numberr+1
