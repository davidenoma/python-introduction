name = "Osarieme"
for ch in name:
    print(ch)
    
print(name[5],name[3], name[1], sep ="")
print(name[-5],name[3], name[-1], sep ="")
print(len(name))


names_crypt = [n+"@" for n in name]
print(names_crypt)
new_name = ""
for i in names_crypt:    
    new_name.join(str(i))
    
print(len(new_name))

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
##print(letters[0:26:2])

print(letters[0:26:2])

text = "Four score and seven years ago"
if 'seven' in text:
    print("The string 'seven'was found.")
else:
    print('The string "seven" was not found')
names = 'Bill joanne Susan Chris Juan Katie'
if 'Pierre' not in names:
    print('Pierre was not found')
else:
    print('Pierre was found')

word = '  member'
print(word)
word_ = word.lstrip()
print(word.lstrip())

ch = "Hello World"
print(ch.replace("World" , "Python" ))
print(ch)

##word_.lstrip("m") == 'm' ? print(hi): print(word_.lstrip("m")
enz = "Pullalanase"
if enz.endswith("ase"):
    print("This is an enzyme")

my_string = "One Two Three " * 3
print(my_string.split())

date_string = '11,12,2020'
print(date_string.split(','))



