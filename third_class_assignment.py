for i in range(5):
    print("Hello World!")
for i in range(10,-1,-1):
    print(i)
for i in range(0,6):    
    print("I love to program!")
    
score = int(input("Enter the test score: "))

while score < 0 and score > 100:
    print("Error: The score cannot be negative and greater than 100")
    score = int(input("Enter the correct score: "))
    
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours,":",minutes,":",seconds)
