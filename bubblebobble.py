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

    def __init__(self, name, min_strength_bonus, max_strength_bonus):
        self.name = name
        self.strength_bonus = random.randint(min_strength_bonus, max_strength_bonus)

player = Player(100, 10, 1)
stick = Item("Pinne", 15,20)
woodenSword = Item("Träsvärd", 20,30)
ironSword = Item("Järnsvärd", 30, 60)

def calculate_total_strength():
    totalStrength = player.strength
    for item in player.inventory:
        totalStrength += item.strength_bonus
    return totalStrength

# Funktion för Start menyn
def start_menu():
    while True:
        slow_print("Välkommen till Sagan Om Dörren\n")
        choice = input("Vill du börja spela? (y/n): ")
        if choice.lower() == "y":
            slow_print("Din uppgift är att passera genom dörrar. Där kan du vänta dig lite olika hinder men om du har tur kan du även hitta en kista.\nFör att vinna spelet måste du nå nivå 10 och det gör du genom att utforska och slåss mot monster.")
            choose_action()
            break
        elif choice.lower() == "n":
            exit()
        else:
            print("Du måste svara y eller n")

def choose_action():
    while True:
        actionChoice = input("\n[1]Kolla ditt inventory\n[2]Kolla dina egenskaper\n[3]Välj en dörr\nVälj ett av alternativen: ")
        if actionChoice == "1":
            if len(player.inventory) > 0:
                slow_print("Detta finns i ditt inventory:\n")
                for item in player.inventory:
                    slow_print(f"{item.name} med {item.strength_bonus} styrka, ")
                break
            else:
                slow_print("Ditt inventory är tomt.")

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

def remove_weakest_item(inventory):
    weakest_item = inventory[0]
    for item in inventory[1:]:
        if item.strength_bonus < weakest_item.strength_bonus:
            weakest_item = item

    index = player.inventory.index(weakest_item)
    player.inventory.pop(index)

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

    stick.strength_bonus = random.randint(10, 20)
    woodenSword.strength_bonus = random.randint(20, 30)
    ironSword.strength_bonus = random.randint(30, 60)

    randomWeapon = random.randint(1,45)
    if randomWeapon <= 25:
        slow_print(f"Du hittade en {stick.name.lower()} med {stick.strength_bonus} styrkepoäng")
        found_item = stick
    elif randomWeapon <= 40:
        slow_print(f"Du hittade ett {woodenSword.name.lower()} med {woodenSword.strength_bonus} styrkepoäng")
        found_item = woodenSword
    elif randomWeapon <= 45:
        slow_print(f"Du hittade ett {ironSword.name.lower()} med {ironSword.strength_bonus} styrkepoäng")
        found_item = ironSword
    if len(player.inventory) >= 5:
        while True:
            changeWeapon = input(f"\nDitt inventory är fullt, vill du byta ut ditt sämsta vapen mot detta? (y/n) ")           
            if changeWeapon.lower() == "y":
                remove_weakest_item(player.inventory)
                player.addItem(found_item)
                break
            elif changeWeapon.lower() == "n":
                break
            else:
                print("Du måste svara y eller n")     
    else:
        player.addItem(found_item)



def main():
    if player.hp <= 0:
        while True:
            playAgain = input("\nDu dog! Vill du börja om? (y/n)")
            if playAgain.lower() == "y":
                player.reset()
                break
            elif playAgain.lower() == "n":
                exit()
            else:
                print("Du måste svara y eller n")
    
    if player.lvl == 10:
        while True:
            playAgain = input("\nGrattis du vann! Vill du spela igen? (y/n)")
            if playAgain.lower() == "y":
                player.reset()
                break
            elif playAgain.lower() == "n":
                exit()
            else:
                print("Du måste svara y eller n")
    choose_action()
    
start_menu()

while True:
    main()