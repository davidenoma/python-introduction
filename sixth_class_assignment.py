import random
  ##Question 1
numbers1 = list(range(5,5*100+5,5))
numbers2 = list()
for i in numbers1:
    numbers2.append(i)
print(numbers2)

##Question 2
def sum_list(list_):
    sum_ = 0
    for num in list_:
        sum_ += num
    return sum_
print(sum_list(numbers2))

#Question 3
names = ['Please', 'Fill', 'Pearl', 'Ruby']
if 'Ruby' in names:
    print('Hello Ruby')
else:
    print('No Ruby')

##Question 4
lottery = list()
i = 0
while i < 7:
    lottery.append(random.randrange(0,10))
    i += 1
    
print(lottery)
j = 0
while j < len(lottery):
    print(lottery[j])
    j+=1
    
##Question 5
print('Rainfall calculator: ')
fallpermonth = []
for i in range(1,13):
    fall = int(input("Enter rainfall for Month: "+str(i)+": "))
    fallpermonth.append(fall)
total = 0 
for i in fallpermonth:
    total += int(i)
print("total is: ", total)
print("average rainfall is: ", total/len(fallpermonth))
print("max rainfall is: ", max(fallpermonth))
print("min rainfall is: ", min(fallpermonth))

    
        
