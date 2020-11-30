y = [1,3,4]
z = y * 2
for i in z:
    print(i)

my_list = [1,2,3,5]
i = 0
while i < 4:
##    print(my_list[i])
    i += 1
my_list = [12, 22, 32, 42]


index = len(my_list) - 1
while index >= 0:
    print(my_list[index])
    index -= 1

    
i = 1
while i <= len(my_list):
    print(my_list[-i])
    i += 1

my_list[1] = 50
print(my_list)

numbers = [1,2,3,4,5]
new_list = my_list + numbers
print(new_list)

days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
print(days[2:5])

numbers = [1,2,3,4,5]
print(numbers[:3])
print(numbers[3:])
print(numbers[:])
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[1:8:2])
print(numbers[1:8:2])
print(numbers[-5:])

prod_nums = ['V475','F987','Q143','R688']
search = input('Enter a product number: ')

if search in prod_nums:
    print(search,' was found! :D')
else:
    print(search, ' was not found! :(')


del numbers[5]
print(numbers)
print(min(numbers))
print(max(numbers))
print(numbers.reverse())
print(numbers)
numbers.insert(2,11)
print(numbers)

def main():
    numbers = [2,4,6,8,10]
    print (' The total is: ', get_total(numbers))
def get_total(value_list):
    total = 0
    for num in value_list:
        total += num
    return total
main()

my_tuple = (1,2,3,4,5,6,5,1)

print(my_tuple)
my_list = list(my_tuple)
my_tuple = tuple(my_list)




            

