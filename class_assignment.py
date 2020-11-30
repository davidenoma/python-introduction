def check():
    password = input("Please enter your password: ")
    if password == "autonomous":
        print("password accepted!")
        return
    else:
        print("Sorry, that is the wrong password")
        check()
check()    

