height = int(input("Please enter your height? " ))
print("Your height is",height, " cm.")
print("-------------------\n\n")
downPayment = 150000
total = 180000
due = total - downPayment 
print("Due payment is:",due)
print("-------------------\n\n")
print(format(1234567.456,'.1f'))
print("-------------------\n\n")
print('George', 'John', 'Paul', 'Ringo', sep='@')
print("-------------------\n\n")

totalSales = int(input("What is the projected amount of total sales? "))
print("Total profit is: ", totalSales * 0.23)

print("-------------------\n\n")
miles = int(input("How many miles driven? "))
gallons = int(input("How many gallons of gas? "))
print("The MPG of your car is ", miles/gallons)
print("-------------------\n\n")
amount = int(input("Charge for food? "))
print("The tip is ", 0.15*amount)
print("The sales tax is ", 0.07 * amount)
print("Your total amount is: ", amount + (0.15 * amount) + (0.07 * amount))

