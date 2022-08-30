import random

random_password = []
lowercase= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase = [lowercase.upper() for lowercase in lowercase]

def small_letters():
    random_password+=random.choices(lowercase, k=2)

def capital_letters():
     random_password+=random.choices(uppercase, k=2)

def num_chars():
    random_password+=random.randint(0,9,k=2)

def special_chars()
    random_password+=random.choices(special_characters,k=2)

def random_password():
    random.shuffle(random_password)
    ''.join(random_password)
    return random_password
    
