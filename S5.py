while True :
    def n_word_r(string, n ):
        word = string.split()
        number_of_n_words = 0
        for myword in word :
            if len(myword)== n:
                print ("found one:", myword)
                number_of_n_words = number_of_n_words+1
        return number_of_n_words
    string = input ("enter str: \n")
    for q in range (1,10):
        kk=n_word_r(string, q)
        print("number of",q,"chaacter words is:" ,kk)
    
    
