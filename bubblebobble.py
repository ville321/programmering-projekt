import random
import time

PRINT_SPEED = 0.035

class Player:

    def __init__(self, hp, strength, lvl):
        self.hp = hp
        self.strength = strength
        self.lvl = lvl

class Item:

    def __init__(self, name, strength_bonus):
        self.name = name
        self.strength_bonus = strength_bonus

player = Player(100, 1, 1)
stick = Item("Pinne", 5)
woodenSword = Item("Träsvärd", random.randint(10,20))
ironSword = Item("Järnsvärd", random.randint(20,50))
inventory = [stick, ironSword, woodenSword, stick]

def addItem(item):
    inventory.append(item)

def calculate_total_strength():
    totalStrength = player.strength
    for item in inventory:
        totalStrength = player.strength + item.strength_bonus
    return totalStrength

# Funktion för Start menyn
def start_menu():
    while True:
        slow_print("Välkommen till Sagan Om Dörren\n")
        choice = input("Vill du börja spela? (y/n): ")
        if choice.lower() == "y":
            slow_print("Din uppgift är att passera genom dörrar. Där kan du vänta dig lite olika hinder men om du har tur kan du även hitta en kista.\nFör att vinna spelet måste du nå nivå 10 och det gör du genom att utforska och slåss mot monster.")
            choose_action()
            return True
        elif choice.lower() == "n":
            break
        else:
            print("Du måste svara y eller n")

def choose_action():
    while True:
        actionChoice = input("\n[1]Kolla ditt inventory\n[2]Kolla dina egenskaper\n[3]Välj en dörr\nVälj ett av alternativen: ")
        if actionChoice == "1":
            slow_print("Detta finns i ditt inventory:\n")
            for item in inventory:
                slow_print(f"{item.name.lower()} med {item.strength_bonus} styrka, ")
            break
        elif actionChoice == "2":
            totalStrength = calculate_total_strength()
            slow_print(f"HP: {player.hp}\nStyrka: {totalStrength}\nNivå: {player.lvl}\n")
            time.sleep(0.5)
            break
        elif actionChoice == "3":
            door()
            break
        else:
            print("Du måste välja mellan 1, 2 eller 3!")
            
def slow_print(txt):
    for letter in txt:
        print(letter, end='', flush = True)
        time.sleep(PRINT_SPEED)

# Funktion för vad som finns bakom dörrarna
def door():
    input("Välj dörr 1, 2 eller 3: ")
    behindDoor = random.randint(1, 3)
    if behindDoor == 1:
        trap()
    elif behindDoor == 2:
        monster()
    elif behindDoor == 3:
        chest()

# Funktion för hur mycket skada fällor ger
def trap():
    trapDamage = random.randint(10, 30)
    player.hp -= trapDamage
    slow_print(f"Du gick in i en fälla och tappade {trapDamage} HP")

# Funktion för monster
def monster():
    totalStrength = calculate_total_strength()
    monsterStrength = random.randint(1, 100)
    print(f"Du stötte på ett monster med {monsterStrength} styrka.")
    if monsterStrength > totalStrength:
        player.hp -= 10
        slow_print(f"Monstret var starkare än dig så du tappade 10 HP!")
    elif monsterStrength < totalStrength:
        player.lvl += 1
        slow_print(f"Du var starkare än monstret så du vann striden. Du gick upp en nivå!")
    elif monsterStrength == totalStrength:
        slow_print(f"Du var lika stark som monstret så striden blev oavgjord!")

#Funktion för kistor
def chest():
    print("Grattis du hittade en kista!")
    randomWeapon = random.randint(1,45)
    if randomWeapon <= 25:
        slow_print(f"Du fick en {stick.name.lower()} med {stick.strength_bonus} styrkepoäng")
        addItem(stick)
    elif randomWeapon <= 40:
        slow_print(f"Du fick ett {woodenSword.name.lower()} med {woodenSword.strength_bonus} styrkepoäng")
        addItem(woodenSword)
    elif randomWeapon <= 45:
        slow_print(f"Du fick ett {ironSword.name.lower()} med {ironSword.strength_bonus} styrkepoäng")
        addItem(ironSword)

# def death_menu():
#     while True:
#         playAgain = input("Du dog! Vill du börja om? (y/n)")
#         if playAgain.lower() == "y":
#             break
#         elif playAgain.lower() == "n":
#             break
#         else:
#             print("Du måste svara y eller n")


def main():
    choose_action()
    # if player.hp <= 0:
    #     death_menu()
    
play = start_menu()
if play == True:
    while True:
        main()