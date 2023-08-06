while True:
    #test 2 to for finding square root
    number = int(input("enter you number: "))
    guess= number / 2
    error = input("enter error: ")
    error = float(error)
    iteration = 0
    while (abs(number -(guess**2))> error):
        iteration = iteration + 1
       # print ("on iteration", iteration , "my guess is ", guess)
        taghsim = number /guess
        guess = (taghsim + guess)/ 2
    print("the square root of", number , "is" , guess)
    
    
