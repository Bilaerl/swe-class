import random

random_password = []
lowercase= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase = [lowercase.upper() for lowercase in lowercase]

def small_letters():
    random_password+=random.choices(lowercase, k=2)

