#test 1 for calculating the area of a pizza
import math
pizza = 10
print ("now we have 10 pizza")
while pizza>0 :
    radius = input("please enter the radius: ")
    r = float(radius)
    #pi = 3.1415
    pi=math.pi
    pizza_area = r**2*pi
    print ("your pizza area is", pizza_area ,"centimeter")
    print ("and int varieble of area is ", pizza_area//1 )
    intvar=int(pizza_area)
    print("area's int variable isssssss" ,intvar) 
    if pizza_area<100:
        print ("too smal pizza", " you cant eat it")
    else :
        print ("enjoy your pizza ")
        pizza = pizza - 1
        if pizza>0 :
             print ("now we have ", pizza , "pizza")
print ("now we dont have pizza")
       
        

