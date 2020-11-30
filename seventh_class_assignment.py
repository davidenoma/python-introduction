choice = input("Please enter your choice: ")
if choice.lower == 'y':
    print("Your choice was yes!")

mystring = "Today is a day of joy"
num = 0 
for ch in mystring:
    if ch == " ":
        num+=1
print("You have ", num ," spaces")
    
print(len(mystring.split(" "))-1)

mystring="aBcdEfghI"
count = 0 
for ch in mystring:
    if ch.islower():
        count+=1
print(count)

def check(arg):
    if arg.endswith('.com'):
        return True
    else:
        return False
    
print(check("hh.com"))

mystring = 'abtcDtEfGhi'
mystring_ = mystring.replace('t','T')
print(mystring_)

mystring="fasdabcdef"
print(mystring[::-3])
print(mystring[-3::])

mystring = 'cookies>milk>fudge>cake>ice cream'
mylist = mystring.split('>')
print(mylist)

name = "John William Smith"
for ch in name.split():
    print(ch[0],'.',sep=" ")

def most_frequent(text):
    max_ = 0
    for i in text:
        if text.count(i) > max_:
            
            max_ = text.count(i)
    return max_

def most_frequent_char(str1):
            dict1 = {}
            max_repeat_count = 0
            for letter in str1:
                    if letter not in dict1:
                            dict1[letter] = 1
                    else:
                            dict1[letter] += 1
                    if dict1[letter]> max_repeat_count:
                            max_repeat_count = dict1[letter]
                            most_repeated_char = letter
            print("The most frequent character is", most_repeated_char, max_repeat_count)
            
most_frequent_char("ddhdhdhddhiiiii")
      


