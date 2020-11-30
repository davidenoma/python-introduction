#Week four Assignment
import random
def times_ten(number):
    
    return int(number) * 10
print(times_ten(49))


rand = random.randrange(8,90)
print(rand)


def half(number):    
    return float(number)/2
print(half(10))


def kinetic_energy(mass,velocity):
    mass = int(input("Please what is your mass in Kg:"))
    velocity = int(input("Please what is your velocity in m/s" ))
    print("The Kinetic Energy is ",(mass*(velocity)**2)/2, "joules " )

kinetic_energy(188,33)


def falling_distance(falling_time):   
        print("The Falling Distance in metres is: ", (9.8*(falling_time)**2)/2)
falling_distance(33)

        
def falling_distance_loop():
    
    for i in range(1,11):
        falling_distance(i)
falling_distance_loop()

def is_prime(number):
    count = 0
    if number > 1:    
        for i in range(2,number):
            if number%i == 0 :            
                count += 1
        if count > 0:
            return False
        else:
            return True
    elif number == 2:
        return True
    else:
        return False
        
def check():
    number = int(input("Please enter a number to check "))
    
    if is_prime(number):
        print("Your number is prime")
    else:
        print("Your number is not prime")
check()



def rand_guess():
    number = random.randint(1,100)
    guess = int(input("Please guess a number"))
    while(guess != number):        
        if guess > number:
            print("Too high, try again")
            continue
        else :
            print("Too low, try again")
            continue

        if guess == number:
            random.randint(1,100)
            print("Your number is correct")
            rand_guess()               
    
rand_guess()
    

    

                

    
    
