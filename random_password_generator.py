"""" this work for making random password

it's give two diff kind of random password
"""
import random

capital_alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small_alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
special_characters = ['!','@','$','#','%','^','&','*','-','_','<','>']
nums = ["0",'1','2','3','4','5','7','8','9']

def capital_selection():


        
        
        capital0 = random.sample(capital_alp,2)
        return capital0
        
        
my_capital = capital_selection()



def small_selection():

    # this select two alp from small_alp and return them,
    
    small0 = random.sample(small_alp,2)

    return small0
        
my_small = small_selection()


def character_selection():

    # this select two charaters from special_character and return them,
 
    character0 = random.sample(special_characters,2)
    
    
    return character0
        

        
my_character = character_selection()

def nums_selection():

    # this select two numbers from num and return them,
     
        num0 = random.sample(nums,2)
        return num0

        
my_num = nums_selection()


def first_main():
    # password = 0
    # while password < 9:
        
    main_password = random.sample(my_capital + my_small + my_character + my_num,8)
        # password += 1
        
    last_password = main_password
    print("".join(last_password))

        
first_main()


def second_main():
    
        my_capital1 =capital_selection()
        my_small1 = small_selection()
        my_character1 = character_selection()
        my_num1 = nums_selection()
        
        last_password = my_capital1 + my_small1 + my_character1 + my_num1
        
        print("".join(last_password))

        
second_main()


