# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 05:33:19 2020

@author: kora
"""
import random
#Question 1 
dic = {'a':1,'b':2,'c':3}

#Question 2 
set1 = set([10,20,30,40,1,2,3])
set2 = set([1,2,3,90,80,70])
set3 = set1.difference(set2)
print(set3)

#Question3
print("Quiz Nigeria")
Nigeria = {'Kebbi':'Birnin Kebbi','Katsina':'Katsina','Edo':'Benin','Osun':'Osogbo'}

keys = list(Nigeria.keys())
questions = 5
i = 0
correct = 0
while i < questions:
    num = random.randint(0,len(Nigeria)-1)
    answer = str(input("What is the capital of "+keys[num]+": "))
    print(answer)
    if Nigeria.get(Nigeria.get(keys[num])) == answer:        
        correct += 1
    i+=1
print("Num correct: ", correct)

#Question 4 
fl = open('cities.txt','r')
words = set()
for ln in fl:
    words.add(ln)
print(words)

#Question 5 
