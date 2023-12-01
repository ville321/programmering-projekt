import random
import time

PRINT_SPEED = 0#.035

class Player:

    def __init__(self, hp, strength, lvl):
        self.hp = hp
        self.strength = strength
        self.lvl = lvl
        self.start_hp = hp
        self.start_strength = strength
        self.start_lvl = lvl
        self.inventory = []

    def reset(self):
        self.hp = self.start_hp
        self.strength = self.start_strength
        self.lvl = self.start_lvl
        self.inventory = []
    
    def addItem(self, item):
        self.inventory.append(item)

class Item:

    def __init__(self, name, strength_bonus):
        self.name = name
        self.strength_bonus = strength_bonus

player = Player(100, 10, 1)

def calculate_total_strength():
    totalStrength = player.strength
    for item in player.inventory:
        totalStrength += item.strength_bonus
    return totalStrength

# Funktion för Start menyn
def start_menu():
    while True:
        slow_print("        Välkommen till Sagan Om Dörren!\n")
        choice = input("\n        Vill du börja spela? (y/n) \n\n        ")
        if choice.lower() == "y":
            choose_action()
            break
        elif choice.lower() == "n":
            exit()
        else:
            print("Du måste svara y eller n")

def choose_action():
    while True:
        actionChoice = input("""\n\n        [1]Kolla ditt inventory     [2]Kolla dina egenskaper        [3]Välj en dörr\n\n        """)
        if actionChoice == "1":
            if len(player.inventory) > 0:
                slow_print("\n        Inventory: ")
                for item in player.inventory:
                    slow_print(f"{item.name} - {item.strength_bonus} styrka | ")
                    input("\n\nTryck \"Enter\" för att fortsätta")
                break
            else:
                slow_print("\n        Ditt inventory är tomt.\n\n")
                input("Tryck \"Enter\" för att fortsätta")

        elif actionChoice == "2":
            totalStrength = calculate_total_strength()
            slow_print(f"\n        HP: {player.hp}\n\n        Styrka: {totalStrength}\n\n        Nivå: {player.lvl}\n\n")
            input("Tryck \"Enter\" för att fortsätta")
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

def remove_weakest_item(inventory):
    weakest_item = inventory[0]
    for item in inventory[1:]:
        if item.strength_bonus < weakest_item.strength_bonus:
            weakest_item = item

    index = player.inventory.index(weakest_item)
    player.inventory.pop(index)

# Funktion för vad som finns bakom dörrarna
def door():
    while True:
        doorChoice = input("""\n        1. Grön dörr        2. Vit dörr        3. Gul dörr\n\n        """)
        if doorChoice == "1" or doorChoice == "2" or doorChoice == "3":
            behindDoor = random.randint(1, 10)
            if behindDoor <= 2:
                trap()
                break
            elif behindDoor <= 6:
                monster()
                break
            elif behindDoor <= 10:
                chest()
                break
        else:
            print("\n        Du måste välja mellan 1, 2 eller 3!")
            input("\n\nTryck \"Enter\" för att fortsätta")
            

# Funktion för hur mycket skada fällor ger
def trap():
    trapDamage = random.randint(10, 20)
    player.hp -= trapDamage
    slow_print(f"\n        Du gick in i en fälla och tappade {trapDamage} HP\n\n")
    input("Tryck \"Enter\" för att fortsätta")

# Funktion för monster
def monster():
    totalStrength = calculate_total_strength()
    if player.lvl <= 3:
        monsterStrength = random.randint(1, 50)
    elif player.lvl <= 5:
        monsterStrength = random.randint(25, 75)
    elif player.lvl <= 10:
        monsterStrength = random.randint(100, 200)
    slow_print(f"\n        Du stötte på ett monster med {monsterStrength} styrka.\n")
    if monsterStrength > totalStrength:
        player.hp -= 10
        slow_print(f"\n        Monstret var starkare än dig så du tappade 10 HP!")
    elif monsterStrength < totalStrength:
        player.lvl += 1
        slow_print(f"\n        Du var starkare än monstret så du vann striden. Du gick upp en nivå!")
    elif monsterStrength == totalStrength:
        slow_print(f"\n        Du var lika stark som monstret så striden blev oavgjord!")
    input("\n\nTryck \"Enter\" för att fortsätta")

#Funktion för kistor
def chest():
    print("\n        Grattis du hittade en kista!")
    randomWeapon = random.randint(1,45)

    if randomWeapon <= 25:
        found_item = Item("Järnrör", random.randint(15,25))
        slow_print(f"\n        Det fanns ett {found_item.name.lower()} med {found_item.strength_bonus} styrkepoäng")
    elif randomWeapon <= 40:
        found_item = Item("Träsvärd", random.randint(30,45))
        slow_print(f"\n        Det fanns ett {found_item.name.lower()} med {found_item.strength_bonus} styrkepoäng")
    elif randomWeapon <= 45:
        found_item = Item("Järnsvärd", random.randint(50,75))
        slow_print(f"\n        Det fanns ett {found_item.name.lower()} med {found_item.strength_bonus} styrkepoäng")

    if len(player.inventory) >= 5:
        while True:
            changeWeapon = input(f"\n\n        Ditt inventory är fullt, vill du byta ut ditt sämsta vapen mot detta? (y/n)\n\n ")           
            if changeWeapon.lower() == "y":
                remove_weakest_item(player.inventory)
                player.addItem(found_item)
                break
            elif changeWeapon.lower() == "n":
                break
            else:
                print("\n        Du måste svara y eller n")     
    else:
        player.addItem(found_item)
    input("\n\nTryck \"Enter\" för att fortsätta")



def main():
    if player.hp <= 0:
        while True:
            playAgain = input("\n       Du dog! Vill du börja om? (y/n)")
            if playAgain.lower() == "y":
                player.reset()
                break
            elif playAgain.lower() == "n":
                exit()
            else:
                print("Du måste svara y eller n")
    
    if player.lvl == 10:
        while True:
            playAgain = input("\n\n       Grattis du vann! Vill du spela igen? (y/n)\n       ")
            if playAgain.lower() == "y":
                player.reset()
                break
            elif playAgain.lower() == "n":
                exit()
            else:
                print("\n       Du måste svara y eller n")
    choose_action()
    
start_menu()

while True:
    main()