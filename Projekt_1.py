"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lejla Sychrová
email: Lejla.Sychrova@seznam.cz
discord: lejlasychrova
"""

texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
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


registrovani = {"bob": "123", "ann": "pass123", 
                "mike": "password123", "liz": "pass123"}
jmeno = input("Username:")
heslo = input("Password:")

pocet_slov = 0
pocet_slov_zac_velke = 0
pocet_slov_velke = 0
pocet_slov_male = 0
pocet_cisel = 0
suma_cisel = 0

if jmeno in registrovani.keys() and heslo == registrovani[jmeno]:
    print("Welcome to the app,", jmeno)
    print("We have 3 texts to be analyzed.")
    print("-"*40)
    volba = int(input("Enter a number btw. 1 and 3 to select: "))
    if volba in range (1,4):
        for slovo in texts[volba-1].split():
            pocet_slov +=1
            if slovo.istitle():
                pocet_slov_zac_velke +=1
            if slovo.isupper():
                pocet_slov_velke +=1
            if slovo.islower():
                pocet_slov_male +=1
            if slovo.isnumeric():
                pocet_cisel +=1
                suma_cisel = suma_cisel + int(slovo)
        print("-"*40)
        print(f"There are {pocet_slov} words in the selected text.")
        print(f"There are {pocet_slov_zac_velke} titlecase words.")
        print(f"There are {pocet_slov_velke} uppercase words.")
        print(f"There are {pocet_slov_male} lowercase words.")
        print(f"There are {pocet_cisel} numeric strings.")
        print(f"The sum of all the numbers is {suma_cisel}.")
        print("-"*40)
        print("LEN|  OCCURENCES      |NR.")
        print("-"*40)

        max_delka = 0
        for slovo in texts[volba-1].split():
            if len(slovo) > max_delka:
                max_delka = len(slovo)
                
        delka = 1
        for delka in range (1, max_delka+1):
            pocet_s_delkou = 0
            for slovo in texts[volba-1].split():
                if len(slovo) == delka:
                    pocet_s_delkou +=1
            print(str(delka).ljust(2),"|",("*"*pocet_s_delkou).ljust(16), "|", pocet_s_delkou)

    else:
        print("Invalid input, terminating the program..")
            
else:
    print("unregistered user, terminating the program..")
