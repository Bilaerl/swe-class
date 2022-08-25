# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 12:25:21 2022

@author: ABUBAKAR BENII
"""

from numpy import random

random_password= []

lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase = []
special_characters = ["!","@","#","$","%","^","&","*","(",")","+","?","/",".",">",",","<","|",";",":","]",":",",","}","[","{","}"]

for i in lowercase:
    uppercase.append(i)
    

def small_letters():
    x=(random.choice(lowercase, size=2))
    global random_password
    for i in x:
        random_password.append(i)


def capital_letters():
    x = random.choice(uppercase, size=2)
    global random_password
    for i in x:
        random_password.append(i)
        
        
def num_chars():
    x = random.randint(0,9, size=2)
    global random_password
    for i in x:
        random_password.append(str(i))

def special_chars():
    x = random.choice(special_characters, size=2)
    global random_password
    for i in x:
        random_password.append(i)
        

def main():
    small_letters()
    capital_letters()
    num_chars()
    special_chars()
    random.shuffle(random_password)
    randomPassword=''
    for i in random_password:
        randomPassword+=i
    print(randomPassword)
main()