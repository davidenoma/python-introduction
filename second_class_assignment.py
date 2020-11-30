def check():
    password = input("Please enter your password: ")
    if password == "autonomous":
        print("password accepted!")
        return
    else:
        print("Sorry, that is the wrong password")
        check()
check()

y,z = 0,0
x = int(input("Please enter a value for x: " ))
if x > 100:
    y = 20
    z = 40
print(" Y is: ", y,"\n", "Z is: ", z)


b = 0
a = int(input(" Please enter a value for b: "))
if a < 10:
    b = 0
else:
    b = 99
print(" B is: ",b)

speed = int(input("What is the speed of the vehicle: " ))
if( speed >= 24 and speed <= 56):
    print(" The speed is normal" )
else:
    print(" Speed is abnormal" )




