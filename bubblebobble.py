import random
import os

inventory = ["hej","hej","hej","hej","Hej","hej"]
class Player:

    def __init__(self, HP, STRENGTH, LVL):
        self.HP = HP
        self.STRENGTH = STRENGTH
        self.LVL = LVL

class Item:

    def __init__(self, name, strength_bonus):
        self.name = name
        self.strength = strength_bonus


player = Player(100, 1, 1)
stick = Item("Pinne", 5)
woodenSword = Item("Träsvärd", random.randint(10,20))
ironSword = Item("Järnsvärd", random.randint(20,50))


def addItem(item):
    inventory.append(item.name)

# Funktion för Start menyn
def start_menu():
    while True:
        choice = input("Vill du börja spela? (y/n): ")
        if choice.lower() == "y":
            print("Din uppgift är att passera genom dörrar. Där kan du vänta dig lite olika hinder men om du har tur kan du även hitta en kista.\nFör att vinna spelet måste du nå nivå 10 och det gör du genom att utforska och slåss mot monster.")
            choose_action()
            break
        elif choice.lower() == "n":
            break
        else:
            print("Du måste svara Y eller N")

def choose_action():
    # os.system('cls')
    while True:
        actionChoice = input("[1]Kolla ditt inventory\n[2]Kolla dina egenskaper\n[3]Välj en dörr\nVälj ett av alternativen: ")
        if actionChoice == "1":
            break
        elif actionChoice == "2":
            print(f"HP: {player.HP}\nStyrka: {player.STRENGTH}\nNivå: {player.LVL}")
            break
        elif actionChoice == "3":
            break
        else:
            print("Du måste välja mellan 1, 2 eller 3!")


# Funktion för vad som finns bakom dörrarna
def door():
    input("Välj dörr 1, 2 eller 3: ")
    behindDoor = random.randint(1, 3)
    if behindDoor == 1:
        trap()
    elif behindDoor == 2:
        #monster()
        pass
    elif behindDoor == 3:
        #chest()
        pass

# Funktion för hur mycket skada fällor ger
def trap():
    trapDamage = random.randint(10, 30)
    player.HP -= trapDamage
    print(f"Du gick in i en fälla och tappade {trapDamage} HP")
    input("Tryck enter för att gå vidare")

def monster():
    monsterStength = random.randint(1, 100)
    if monsterStength > player.STRENGTH:
        player.HP -= 10
        print(f"Du stötte på en monster med")
    pass

def chest():
    print("Grattis du hittade en kista!")
    randomWeapon = random.randint(1,45)
    if randomWeapon <= 25:
        print(f"Du fick en {stick.name.lower()} med {stick.strength} styrkepoäng")
        addItem(stick)
    elif randomWeapon <= 40:
        print(f"Du fick ett {woodenSword.name.lower()} med {woodenSword.strength} styrkepoäng")
        addItem(woodenSword)
    elif randomWeapon <= 45:
        print(f"Du fick ett {ironSword.name.lower()} med {ironSword.strength} styrkepoäng")
        addItem(ironSword)
    else:
        print("Kistan var tom! ")

def main():
    choose_action()
    

play = start_menu()
if play == True:
    while True:
        main()