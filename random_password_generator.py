# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 20:34:24 2022

@author: ABUBAKAR BENII
"""

import random

randompassword=[]
lower =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper=[i.upper() for i in lower]
special_xters = ["!","@","#","$","%","^","&","*","(",")","+","?","/",".",">",",","<","|",";",":","]",":",",","}","[","{","}"]

def small():
    global randompassword
    randompassword+=random.choices(lower,k=2)
    
def capital():
    global randompassword
    randompassword+=random.choices(upper,k=2)
    
def special():
    global randompassword
    randompassword+=random.choices(special_xters,k=2)
    
def numerical():
    global randompassword
    randompassword+=random.choices(range(10),k=2)
    
def random_password():
    global randompassword
    random.shuffle(randompassword)
    randompassword= ''.join(str(i) for i in randompassword)
    print(randompassword)

def main():
    small()
    capital()
    special()
    numerical()
    random_password()
    
    
main()

