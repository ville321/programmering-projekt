import random
import time

PRINT_SPEED = 0#.035
SCENARIOPRINT_SPEED = 1.5


class Player:#Klass för spelaren

    def __init__(self, hp, strength, lvl):
        self.hp = hp
        self.strength = strength
        self.lvl = lvl
        #self.start variablerna används för att spara originala värdena utan att variablarna ändras som variablarna ovanför gör under programmet.
        self.start_hp = hp 
        self.start_strength = strength
        self.start_lvl = lvl
        self.inventory = []

    def reset(self): #Sätter hp, lvl, styrka och inventory till originala värden när funktionen kallas. 
        self.hp = self.start_hp
        self.strength = self.start_strength
        self.lvl = self.start_lvl
        self.inventory = []
    
    def addItem(self, item): #Sätter in "item" i inventory listan
        self.inventory.append(item)


class Item:#klass för items

    def __init__(self, name, strength_bonus):
        self.name = name
        self.strength_bonus = strength_bonus

player = Player(100, 10, 1)

def calculate_total_strength(): #Används för att räkna ut spelarens totala styrka (spelarens styrka + vapnenas kombinerade styrkebonus)
    totalStrength = player.strength
    for item in player.inventory:
        totalStrength += item.strength_bonus
    return totalStrength


def start_menu():# Funktion för Start menyn
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

def choose_action(): #Loop som programmet hela tiden kommer tillbaka till. Där man får göra sina val. 
    while True:
        actionChoice = input("""\n\n        [1]Kolla ditt inventory     [2]Kolla dina egenskaper        [3]Välj en dörr\n\n        """)
        if actionChoice == "1":
            if len(player.inventory) > 0: #Kollar om inventoryt är tomt. Om det är tomt printar den att det är tomt annars printar det innehåller i inventoryt.
                slow_print("\n        Inventory: ")
                for item in player.inventory:
                    slow_print(f"{item.name} - {item.strength_bonus} styrka | ")
                input("\n\nTryck \"Enter\" för att fortsätta")
                break
            else:
                slow_print("\n        Ditt inventory är tomt.\n\n")
                input("Tryck \"Enter\" för att fortsätta")

        elif actionChoice == "2":
            totalStrength = calculate_total_strength()#Skriver ut spelarens egenskaper.
            slow_print(f"\n        HP: {player.hp}\n\n        Styrka: {totalStrength}\n\n        Nivå: {player.lvl}\n\n")
            input("Tryck \"Enter\" för att fortsätta")
            break
        elif actionChoice == "3":#Kallar på door() funktionen.
            door()
            break
        else:#Gör att loopen börjar om ifall man svarar något annat än alternativen
            print("Du måste välja mellan 1, 2 eller 3!")
            
def slow_print(txt):#tar en string och skriver ut varje bokstav för sig med lite mellanrum för att få ett finare print
    for letter in txt:
        print(letter, end='', flush = True)
        time.sleep(PRINT_SPEED)

def find_weakest_item(inventory):#Antar att första objektet i inventory är det svagaste och jämför det sedan med resterande objekt och sätter det svagaste till weakest_item
    weakest_item = inventory[0]
    for item in inventory[1:]:
        if item.strength_bonus < weakest_item.strength_bonus:
            weakest_item = item
    return weakest_item

def remove_weakest_item(item):#Tar bort svagaste objektet från inventoryt. Find_weakest_item och den här funktionen är separata för att lätt kunna printa det svagaste föremålet utan att ta bort det.
    item = find_weakest_item(player.inventory)
    index = player.inventory.index(item)
    player.inventory.pop(index)


def door():# Funktion för vad som finns bakom dörrarna
    while True:
        doorChoice = input("""\n        1. Grön dörr        2. Vit dörr        3. Gul dörr\n\n        """)
        if doorChoice == "1" or doorChoice == "2" or doorChoice == "3":
            behindDoor = random.randint(1, 10)#Istället för att slumpa mellan 1 till 3 har vi såhär så att man kan styra oddsen.
            if behindDoor <= 1:
                trap()
                break
            elif behindDoor <= 7:
                result, monsterStrength = monster()
                different_scenarios(result, monsterStrength)
                break
            elif behindDoor <= 10:
                chest()
                break
        else:
            print("\n        Du måste välja mellan 1, 2 eller 3!")
            input("\n\nTryck \"Enter\" för att fortsätta")
            


def trap():# Funktion för fällor. Tre scenarion som det slumpas mellan för lite variation i spelupplevelsen.
    trapDamage = random.randint(10, 20)
    player.hp -= trapDamage
    trapScenario = random.randint(1, 3)
    if trapScenario == 1:
        print(f"\n        ***Du trampar på en dold fallucka och förlorar {trapDamage} HP!***")
        time.sleep(SCENARIOPRINT_SPEED)
        print("\n        ***Smärtan skär genom dig när du känner spikarna under dina fötter.***")
        time.sleep(SCENARIOPRINT_SPEED)
        print("\n        ***Med kraft tar du dig upp och fortsätter din färd.***")
        time.sleep(SCENARIOPRINT_SPEED)
    elif trapScenario == 2:
        print(f"\n        ***Plötsligt aktiveras en fördold snärjning, och du tar {trapDamage} HP skada!***")
        time.sleep(SCENARIOPRINT_SPEED)
        print("\n        ***Du undrar hur du kunde missa den listiga fällan, men du går vidare med försiktighet.***")
        time.sleep(SCENARIOPRINT_SPEED)
    elif trapScenario == 3:
        print(f"\n        ***En dold mekanism utlöses, och du förlorar {trapDamage} HP!***")
        time.sleep(SCENARIOPRINT_SPEED)
        print("\n        ***Du tar dig samman och fortsätter din resa.***")
        time.sleep(SCENARIOPRINT_SPEED)
    input("\n\nTryck \"Enter\" för att fortsätta")

def different_scenarios(result, monsterStrength):#De olika scenariona när man stöter på ett monster. Det finns tre scenarion med tre versioner ifall man vinner, förlorar eller om det blir lika.
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


def monster():# Funktion för monster
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



def chest():#Funktion för kistor
    randomWeapon = random.randint(1,45)
    if randomWeapon <= 25:
        found_item = Item("Träsvärd", random.randint(15,25))
    elif randomWeapon <= 40:
        found_item = Item("Järnsvärd", random.randint(30,45))
    elif randomWeapon <= 45:
        found_item = Item("Guldsvärd", random.randint(50,75))

    chestScenario = random.randint(1, 3)
    if chestScenario == 1:
        print("\n        ***Du hittar en gammal kista dold bland ruinerna. Du öppnar den försiktigt.***")
        time.sleep(SCENARIOPRINT_SPEED)
        print(f"\n        ***Inuti hittar du ett {found_item.name.lower()} med {found_item.strength_bonus} styrkepoäng!***")
        time.sleep(SCENARIOPRINT_SPEED)
    elif chestScenario == 2:
        print("\n        ***När du vandrar genom skogen, upptäcker du en gömd skattkista.***")
        time.sleep(SCENARIOPRINT_SPEED)
        print(f"\n        ***Inuti finner du ett {found_item.name.lower()} med {found_item.strength_bonus} styrkepoäng!***")
        time.sleep(SCENARIOPRINT_SPEED)
    elif chestScenario == 3:
        print("\n        ***I distansen ser du någonting lysa.***")
        time.sleep(SCENARIOPRINT_SPEED)
        print("\n        ***Du springer dit och hittar en guldig kista.***")
        time.sleep(SCENARIOPRINT_SPEED)
        print(f"\n        ***Bland skatten finns ett {found_item.name.lower()} med {found_item.strength_bonus} styrkepoäng!***")
        time.sleep(SCENARIOPRINT_SPEED)
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



def main():#Huvudloopen
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