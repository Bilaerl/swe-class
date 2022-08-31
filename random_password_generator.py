"""This program generates a string containing eight random characters, two each of 
capital letters, small letters, numerical characters and special character,
using the python built-in random module
""""


import random

random_password = []
lowercase= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase = [lowercase.upper() for lowercase in lowercase]
special_characters = ["!","@","#","$","%","^","&","*","(",")","+","?","/",".",">",",","<","|",";",":","]",":",",","}","[","{","}"]

def small_letters():
    
    """randomly picks two elements from the lowercase list 
        and adds them to the random_password list"""
        
    random_password+=random.choices(lowercase, k=2)


def capital_letters():
    """randomly picks two elements from the uppercase list 
        and adds them to the random_password list"""
        
     random_password+=random.choices(uppercase, k=2)


def num_chars():
    """picks two random integers from 0 to 10 
        and adds them to the random_password list"""
        
    random_password+=random.choices(range(10),k=2)


def special_chars():
    """randomly picks two elements from the special_characters list 
        and adds them to the random_password list"""
        
    random_password+=random.choices(special_characters,k=2)


def random_password():
    
    """shuffles the random_password list
    and forms a string using the join() method
    returns the formed string
    """
    
    random.shuffle(random_password)
    ''.join(str(random_password) for random_password in random_password)
    return random_password

def main():
    """"calls all the functions above
    """
    small_letters()
    capital_letters()
    num_chars()
    special_chars()
    random_password()
    
main()
