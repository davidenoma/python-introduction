import random
def main():
    cities = ['New york','Boston', 'Atlanta', 'Dallas']
    outfile = open('cities.txt','w')

    for item in cities:
        outfile.write(item + '\n')
        
    outfile.close()
    
#Question1
    file = open('number_list.txt', 'a')
    for i in range(1,6):
        file.write(str(i)+"\n")

    file.close()

#Question 2
    file = open('number_list.txt','r')
    for ln in file:
        print(ln)
    file.close()
    
#Question 3
    file = open('number_list.txt','r')
    total = 0
    for ln in file:
        print(ln)
        total += int(ln)
    print("\n", "The sum is: ",total)
    file.close()    

#Question 4
    numRand = int(input("How many Random numbers do you want to generate? "))
    rands = open('randnos.txt','w')
    for i in range(1, numRand+1):
        rands.write(str(random.randint(1,100))+"\n")
                    
    rands.close()

#Question 5
    rands = open('randnos.txt','r')
    total = 0
    count = 0 
    for ln in rands:
        total += int(ln)
        count += 1       
    print("Total is: ", total)
    print("Number of Random Numbers is: ",count)
    rands.close()

#Question 6
    integers = open('randnos.txt','r')
    for ln in integers:
        total += int(ln)
        count += 1 
    try:
        print("Average of all numbers is: ", total/count)
    except IOError:
        print("File is opened ad data is read from it ")
    except ValueError:
        print("Items read from the file are converted to a number")      
    integers.close()

#Question 7
    print("Welcome to Spring Fork Amateur Golf Club")
    print("-----------------------------------------")
    print("When done enter 'done' as a value")
    golf = open("golf.txt", "w")
    golf.write("Name"+"\t"+"Score\n")
    golf.close()
    check = True
    while (check == True):
        
        name = input("Player's Name: ")
        if name == "done" :
            break 
        score = int(input("Player's Score: "))
              
        golf = open("golf.txt", "a")
        golf.write(name + "\t" + str(score) + "\n")
        golf.close()
    print("Finished...")

#Question 8
    golf = open('golf.txt', 'r')

    for ln in golf:
        print(ln)
    golf.close()

main()
