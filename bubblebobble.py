import random
import os
class Player:

    def __init__(self, HP, STRENGTH, LVL):
        self.HP = HP
        self.STRENGTH = STRENGTH
        self.LVL = LVL

class Item:

    def __init__(self) -> None:
        pass

player = Player(100, 10, 1)

# Funktion för Start menyn
def start_menu():
    while True:
        choice = input("Vill du börja spela? (y/n): ")
        if choice == "y":
            print("Din uppgift är att passera genom dörrar, vid varje dörr får du antigen öppna en kista, slåss mot ett monster eller så snubblar du in i en fälla. \nÄr det en kista bakom dörren får du ett nytt svärd med slumpmässig styrka \n Är det en fälla bakom dörren tar du skada\n Är det ett monster bakom dörren utbrister en strid, förlorar du striden tar du 10 skada, vinner du striden går du upp i nivå \nSpelet är avklarat när du nått nivå 10 ")
            break
        elif choice == "n":
            print("Spelet Avslutat")
            break
        else:
            print("Du måste svara Y eller N")

def choose_action():
    # os.system('cls')
    while True:
        actionChoice = input("[1]Kolla ditt inventory\n[2]Kolla dina egenskaper\n[3]Välj en dörr\n")
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

def main():
    start_menu(False)
    
# main()
choose_action()