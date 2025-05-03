"""
project_1.py: první projekt do Engeto Online Python Akademie

author: Tomáš Zbořil
email: tomas.zboril@seznam.cz
"""
import string

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

user = ["bob", "ann", "mike", "liz"]
password = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}


jmeno = input("username: ")
heslo = input("password: ")

if jmeno in user and password[jmeno] == heslo:
    print("-" * 40)
    print("Welcome to the app,", jmeno)
    print("We have 3 texts to be analyzed.")
    print("-" * 40)
else:
    print("unregistered user, terminating the program..")
    exit()
   
cislo =  input("Enter a number btw. 1 and 3 to select: ")

if not cislo.isdigit():
    print("The number of a text is not entered.")
    exit()

if not int(cislo) in range(1,4):
    print("The selected text does not exist.")
    exit()

index = int(cislo) - 1
text =  TEXTS[index]

slova = text.split()
slova_ocistena = [slovo.strip(string.punctuation) for slovo in slova]

pocet_slov = len(slova_ocistena)
mala = 0
velka = 0
prvni = 0
pocet_cisel = 0
suma = 0

for slovo in slova_ocistena:
    if slovo.islower():
        mala += 1
    if slovo.isupper():
        velka += 1
    if slovo.istitle():
        prvni += 1       
    if slovo.isnumeric():
        pocet_cisel += 1  
        suma += int(slovo)

print("-" * 40)     
print("There are", pocet_slov, "words in the selected text.")
print("There are", prvni, "titlecase words.") 
print("There are", velka, "uppercase words.") 
print("There are", mala, "lowercase words.")
print("There are", pocet_cisel, "numeric strings.")
print("The sum of all the numbers", suma)
print("-" * 40)
print("LEN|   OCCURENCES   |NR.")
print("-" * 40)

delky_slov = [len(slovo) for slovo in slova_ocistena]

for delka in range (1,max(delky_slov)+1):
    vyskyt = delky_slov.count(delka)
    if vyskyt > 0:
        print(f"{delka:>3}|{'*' * vyskyt:<16}|{vyskyt}")        

    
    




