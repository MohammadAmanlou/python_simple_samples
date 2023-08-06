#show if the number is prime or not and list the prime number from 1 to x
import time
t=time.time()
while True:
    r=0
    this_number= 1
    x = int(input("enter the number: "))
    if (x ==1 or x==0):
        print ("not prime")
    while(this_number<x-1):
        this_number = this_number + 1
        if(x%this_number==0):
            r= r+1
            if (r==1):
                print ("not prime")
                break
    if (r!= 1 and x!=0 and x!= 1):
        print("prime")
    t2=time.time()
    print(t2-t)
    this_numberr=2
    while (this_numberr<x+1):
        is_prime_number = True
        counter=2
        while (counter< (this_numberr-1)):
            if (((this_numberr) % counter)==0):
                is_prime_number = False
                break
            counter= counter +1
        if (is_prime_number== True):
            print (this_numberr)
        this_numberr= this_numberr+1
