import random
import time

PRINT_SPEED = 0#.035
SCENARIOPRINT_SPEED = 1.5

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

def find_weakest_item(inventory):
    weakest_item = inventory[0]
    for item in inventory[1:]:
        if item.strength_bonus < weakest_item.strength_bonus:
            weakest_item = item
    return weakest_item

def remove_weakest_item(item):
    item = find_weakest_item(player.inventory)
    index = player.inventory.index(item)
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
                result, monsterStrength = monster()
                different_scenarios(result, monsterStrength)
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

def different_scenarios(result, monsterStrength):
    randomScenario = random.randint(1,3)
    if randomScenario == 1:
        if result== "win":            
            print(f"\n        ***Ett troll med {monsterStrength} styrka dyker upp framför dig***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Trollet svingar sin slägga mot dig***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Du slänger dig åt sidan och hugger sedan trollet med ditt vassa svärd.***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Trollet faller ned på marken med ett duns***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        Du besegrade trollet och gick upp en nivå")
        elif result == "loss":
            print(f"\n        ***Ett troll med {monsterStrength} styrka dyker upp framför dig***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Trollet svingar sin slägga mot dig***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Du försöker ducka men är för långsam och blir träffad***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Du flyr från trollet och springer vidare.***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        Du blev skadad av trollet och förlorade 10 HP")
        elif result == "tie":
            print(f"\n        ***Ett troll med {monsterStrength} styrka dyker upp framför dig***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Du tar fram ditt svärd och trollet tar fram sin gigantiska slägga***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Ni båda inser att ingen kommer vinna striden utan stora skador***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Trollet går sin väg och du fortsätter på ditt äventyr***")
            time.sleep(SCENARIOPRINT_SPEED)
    elif randomScenario == 2:
        if result == "win":            
            print(f"\n        ***En majestätisk elddrake med {monsterStrength} styrka stiger fram ur lågorna framför dig***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Elddraken rusar mot dig med eldsflammor dansande runt dess skarpa klor. Du duckar och hugger till med ditt svärd.***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Du lyckas träffa elddrakens svans, och den rullar i smärta. Elddraken sänker sig ner och ger upp.***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        Elddraken besegrad! Du känner en varm kraft inom dig och går upp en nivå.")
        elif result == "loss":
            print(f"\n        ***En majestätisk elddrake med {monsterStrength} styrka stiger fram ur lågorna framför dig***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Du försöker parera elddrakens flammor, men en eldboll träffar dig. Du känner värmen bränna och förlorar 10 HP.***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Elddraken skrattar och flyger bort.***")
        elif result == "tie":
            print(f"\n        ***En majestätisk elddrake med {monsterStrength} styrka stiger fram ur lågorna framför dig***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Du möter elddraken med ditt svärd redo för strid. Ni båda går till attack men efter några slag inser ni att det är i förgäves.***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Efter en kort konfrontation flyger elddraken bort och lämnar dig oskadd. Du fortsätter ditt äventyr.***")
    elif randomScenario == 3:
        if result == "win":            
            print(f"\n        ***En forntida jordgolem med {monsterStrength} styrka reser sig ur marken framför dig***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Golemen rusar mot dig med steniga nävar, men du undviker smidigt och kontrar med ditt vassa svärd.***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Du lyckas hugga av golemens stenarmar och träffa dess svaga punkt. Golemen kollapsar till stendamm.***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        Jordgolem besegrad och du går upp en nivå!")
        elif result == "loss":
            print(f"\n        ***En forntida jordgolem med {monsterStrength} styrka reser sig ur marken framför dig***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Golemen slår till med sina massiva nävar, och du försöker undvika dem, men blir träffad. Du förlorar 10 HP.***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Golemen skrattar med sitt stenansikte och sänker sig tillbaka i marken.***")
        elif result == "tie":
            print(f"\n        ***En forntida jordgolem med {monsterStrength} styrka reser sig ur marken framför dig***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Du och golem står emot varandra, redo för strid. Golemen verkar känna din beslutsamhet och drar sig tillbaka.***")
            time.sleep(SCENARIOPRINT_SPEED)
            print("\n        ***Du fortsätter ditt äventyr, och golemen sänker sig tillbaka i marken, låtandes dig vara i fred.***")
    input("\n\nTryck \"Enter\" för att fortsätta")

# Funktion för monster
def monster():
    totalStrength = calculate_total_strength()
    if player.lvl <= 3:
        monsterStrength = random.randint(1, 50)
    elif player.lvl <= 5:
        monsterStrength = random.randint(25, 75)
    elif player.lvl <= 10:
        monsterStrength = random.randint(100, 200)

    if monsterStrength > totalStrength:
        player.hp -= 10
        result = "loss"
    elif monsterStrength < totalStrength:
        player.lvl += 1
        result = "win"
    else:
        result = "tie"
    return result, monsterStrength


#Funktion för kistor
def chest():
    randomWeapon = random.randint(1,45)
    if randomWeapon <= 25:
        found_item = Item("Träsvärd", random.randint(15,25))
        slow_print(f"\n        Du hittade en kista med ett {found_item.name.lower()} som har {found_item.strength_bonus} styrkepoäng")
    elif randomWeapon <= 40:
        found_item = Item("Järnsvärd", random.randint(30,45))
        slow_print(f"\n        Du hittade en kista med ett {found_item.name.lower()} som har {found_item.strength_bonus} styrkepoäng")
    elif randomWeapon <= 45:
        found_item = Item("Guldsvärd", random.randint(50,75))
        slow_print(f"\n        Du hittade en kista med ett {found_item.name.lower()} som har {found_item.strength_bonus} styrkepoäng")

    if len(player.inventory) >= 5:
        while True:
            changeWeapon = input(f"\n\n        Ditt inventory är fullt, vill du byta ut ditt sämsta vapen som har {find_weakest_item(player.inventory).strength_bonus} styrka, mot detta? (y/n)\n\n        ")           
            if changeWeapon.lower() == "y":
                remove_weakest_item(find_weakest_item(player.inventory))
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
        slow_print("\n\n        Du har övervunnit alla faror, besegrat skräckinjagande monster och plundrat gömda kistor.")
        time.sleep(SCENARIOPRINT_SPEED)
        slow_print("\n        Ditt mod och din skicklighet har tagit dig genom de mystiska dörrarna och överlevt det okända.")
        time.sleep(SCENARIOPRINT_SPEED)
        slow_print("\n        När du öppnar den sista dörren, strålar ljuset in och en känsla av triumf fyller ditt hjärta.")
        time.sleep(SCENARIOPRINT_SPEED)
        slow_print("\n        Plötsligt hör du en dånande röst från det förflutna, en röst som hyllar din styrka och mod.")
        time.sleep(SCENARIOPRINT_SPEED)
        slow_print("\n        \"Du, modige äventyrare, har klarat prövningarna och bevisat dig vara en sann hjälte!\"")
        time.sleep(SCENARIOPRINT_SPEED)
        slow_print("\n        Ditt namn kommer att bli känt och berättat i hela landet som den som erövrade Sagan Om Dörren.")
        time.sleep(SCENARIOPRINT_SPEED)
        slow_print("\n        Du står där, omgiven av ära och seger, redo för nya äventyr och oviss framtid.")
        time.sleep(SCENARIOPRINT_SPEED)
        slow_print("\n        Tack för att du deltog i Sagan Om Dörren!\n\n")
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