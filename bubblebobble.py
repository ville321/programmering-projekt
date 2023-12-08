import random
import time
import os

PRINT_SPEED = 0.035
SCENARIOPRINT_SPEED = 1.5

def clear():
    input("\n(Tryck \"Enter\" för att fortsätta)")
    os.system('cls')

def section():
    print("        ___________________________________________________________________________")

def slow_print(txt):#tar en string och skriver ut varje bokstav för sig med lite mellanrum för att få ett finare print
    for letter in txt:
        print(letter, end='', flush = True)
        time.sleep(PRINT_SPEED)

def print_list_slow(list):#Tar emot en lista och skriver ut varje föremål i listan med en liten delay
    for i in list:
        print(i)
        time.sleep(SCENARIOPRINT_SPEED)

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
    os.system('cls')
    slow_print("        Välkommen till Sagan Om Dörren!\n")
    while True:
        choice = input("\n        Vill du börja spela? (y/n) \n\n        ")
        if choice.lower() == "y":
            choose_action()
            break
        elif choice.lower() == "n":
            exit()
        else:
            section()
            print("\n        Du måste svara y eller n")

def choose_action(): #Loop som programmet hela tiden kommer tillbaka till. Där man får göra sina val. 
    while True:
        os.system('cls')
        actionChoice = input("""\n\n        [1]Kolla ditt inventory     [2]Kolla dina egenskaper        [3]Välj en dörr\n\n        """)
        if actionChoice == "1":
            os.system('cls')
            section()
            if len(player.inventory) > 0: #Kollar om inventoryt är tomt. Om det är tomt printar den att det är tomt annars printar det innehåller i inventoryt.
                print("\n        Inventory: ", end='')
                for item in player.inventory:
                    print(f"\n          {item.name} - {item.strength_bonus} styrka", end='') 
                print("")
                section()
                clear()
                break
            else:
                print("\n        Ditt inventory är tomt.\n")
                section()
                clear()

        elif actionChoice == "2":
            os.system('cls')
            totalStrength = calculate_total_strength()#Skriver ut spelarens egenskaper.
            section()
            print(f"\n        Egenskaper:\n\n            HP: {player.hp}\n\n            Styrka: {totalStrength}\n\n            Nivå: {player.lvl}\n")
            section()
            clear()
            break
        elif actionChoice == "3":#Kallar på door() funktionen.
            os.system('cls')
            door()
            break
        else:#Gör att loopen börjar om ifall man svarar något annat än alternativen
            section()
            print("\n        Du måste välja mellan 1, 2 eller 3!")
            clear()

def doorText(door):
    if door == '1':
        return "***Du öppnar och stiger in i rummet genom den gröna dörren***"
    elif door == '2':
        return "***Du öppnar och stiger in i rummet genom den vita dörren***"
    elif door == '3':
        return "***Du öppnar och stiger in i rummet genom den gula dörren***"

def find_weakest_item(inventory):#Antar att första objektet i inventory är det svagaste och jämför det sedan med resterande objekt och sätter det svagaste till weakest_item
    weakest_item = inventory[0]
    for item in inventory[1:]:
        if item.strength_bonus < weakest_item.strength_bonus:
            weakest_item = item
    return weakest_item

def remove_weakest_item():#Tar bort svagaste objektet från inventoryt. Find_weakest_item och den här funktionen är separata för att lätt kunna printa det svagaste föremålet utan att ta bort det.
    item = find_weakest_item(player.inventory)
    index = player.inventory.index(item)
    player.inventory.pop(index)

def door():# Funktion för vad som finns bakom dörrarna
    while True:
        os.system('cls')
        print("                   Välj en dörr att utforska:")
        doorChoice = input("""\n        [1]Grön dörr        [2]Vit dörr        [3]Gul dörr\n\n        """)
        if doorChoice == "1" or doorChoice == "2" or doorChoice == "3":
            os.system('cls')
            behindDoor = random.randint(1, 10)#Istället för att slumpa mellan 1 till 3 har vi såhär så att man kan styra oddsen.
            if behindDoor <= 1:
                trap(doorChoice)
                break
            elif behindDoor <= 6:
                result, monsterStrength = monster()
                different_monster_scenarios(result, monsterStrength, doorChoice)
                break
            elif behindDoor <= 10:
                chest(doorChoice)
                break
        else:
            section()
            print("\n        Du måste välja mellan 1, 2 eller 3!")
            clear()

def trap(doorChoice):# Funktion för fällor. Tre scenarion som det slumpas mellan för lite variation i spelupplevelsen.
    trapDamage = random.randint(10, 20)
    player.hp -= trapDamage
    trapScenario = random.randint(1, 3)
    print(f"\n        {doorText(doorChoice)}")
    time.sleep(SCENARIOPRINT_SPEED)
    if trapScenario == 1:
        print_list_slow([
            f"\n        ***Du trampar på en dold fallucka och förlorar {trapDamage} HP!***",
            "\n        ***Smärtan skär genom dig när du känner spikarna under dina fötter.***",
            "\n        ***Med kraft tar du dig upp och fortsätter din färd.***"
        ])
    elif trapScenario == 2:
        print_list_slow([
            f"\n        ***Plötsligt aktiveras en fördold snärjning, och du tar {trapDamage} HP skada!***",
            "\n        ***Du undrar hur du kunde missa den listiga fällan, men du går vidare med försiktighet.***",
        ])
    elif trapScenario == 3:
        print_list_slow([
            f"\n        ***En dold mekanism utlöses, och du förlorar {trapDamage} HP!***",
            "\n        ***Du tar dig samman och fortsätter din resa.***"
        ])
    clear()

def different_monster_scenarios(result, monsterStrength, doorChoice):#De olika scenariona när man stöter på ett monster. Det finns tre scenarion med tre versioner ifall man vinner, förlorar eller om det blir lika.
    randomScenario = random.randint(1,3)
    print(f"\n        {doorText(doorChoice)}")
    time.sleep(SCENARIOPRINT_SPEED)
    if randomScenario == 1:
        if result== "win":     
            print_list_slow([
                f"\n        ***Ett troll med {monsterStrength} styrka dyker upp framför dig***",
                "\n        ***Trollet svingar sin slägga mot dig***",
                "\n        ***Du slänger dig åt sidan och hugger sedan trollet med ditt vassa svärd.***",
                "\n        ***Trollet faller ned på marken med ett duns***",
                "\n        Du besegrade trollet och gick upp en nivå"
            ])  
        elif result == "loss":
            print_list_slow([
                f"\n        ***Ett troll med {monsterStrength} styrka dyker upp framför dig***",
                "\n        ***Trollet svingar sin slägga mot dig***",
                "\n        ***Du försöker ducka men är för långsam och blir träffad***",
                "\n        ***Du flyr från trollet och springer vidare.***",
                "\n        Du blev skadad av trollet och förlorade 10 HP"
            ])
        elif result == "tie":
            print_list_slow([
                f"\n        ***Ett troll med {monsterStrength} styrka dyker upp framför dig***",
                "\n        ***Du tar fram ditt svärd och trollet tar fram sin gigantiska slägga***",
                "\n        ***Ni båda inser att ingen kommer vinna striden utan stora skador***",
                "\n        ***Trollet går sin väg och du fortsätter på ditt äventyr***"
            ])
    elif randomScenario == 2:
        if result == "win":        
            print_list_slow([
                f"\n        ***En majestätisk elddrake med {monsterStrength} styrka stiger fram ur lågorna framför dig***",
                "\n        ***Elddraken rusar mot dig med eldsflammor dansande runt dess skarpa klor. Du duckar och hugger till med ditt svärd.***",
                "\n        ***Du lyckas träffa elddrakens svans, och den rullar i smärta. Elddraken sänker sig ner och ger upp.***",
                "\n        Elddraken besegrad! Du känner en varm kraft inom dig och går upp en nivå."
            ])
        elif result == "loss":
            print_list_slow([
                f"\n        ***En majestätisk elddrake med {monsterStrength} styrka stiger fram ur lågorna framför dig***",
                "\n        ***Du försöker parera elddrakens flammor, men en eldboll träffar dig. Du känner värmen bränna och förlorar 10 HP.***",
                "\n        ***Elddraken skrattar och flyger bort.***"
            ])
        elif result == "tie":
            print_list_slow([
                f"\n        ***En majestätisk elddrake med {monsterStrength} styrka stiger fram ur lågorna framför dig***",
                "\n        ***Du möter elddraken med ditt svärd redo för strid. Ni båda går till attack men efter några slag inser ni att det är i förgäves.***",
                "\n        ***Efter en kort konfrontation flyger elddraken bort och lämnar dig oskadd. Du fortsätter ditt äventyr.***"
            ])
    elif randomScenario == 3:
        if result == "win":    
            print_list_slow( [
                f"\n        ***En forntida jordgolem med {monsterStrength} styrka reser sig ur marken framför dig***",
                "\n        ***Golemen rusar mot dig med steniga nävar, men du undviker smidigt och kontrar med ditt vassa svärd.***",
                "\n        ***Du lyckas hugga av golemens stenarmar och träffa dess svaga punkt. Golemen kollapsar till stendamm.***",
                "\n        Jordgolem besegrad och du går upp en nivå!"
            ])
        elif result == "loss":
            print_list_slow([
                f"\n        ***En forntida jordgolem med {monsterStrength} styrka reser sig ur marken framför dig***",
                "\n        ***Golemen slår till med sina massiva nävar, och du försöker undvika dem, men blir träffad. Du förlorar 10 HP.***",
                "\n        ***Golemen skrattar med sitt stenansikte och sänker sig tillbaka i marken.***"
            ])
        elif result == "tie":
            print_list_slow([
                f"\n        ***En forntida jordgolem med {monsterStrength} styrka reser sig ur marken framför dig***",
                "\n        ***Du och golem står emot varandra, redo för strid. Golemen verkar känna din beslutsamhet och drar sig tillbaka.***",
                "\n        ***Du fortsätter ditt äventyr, och golemen sänker sig tillbaka i marken, låtandes dig vara i fred.***"
            ])
    clear()
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

def chest(doorChoice):#Funktion för kistor
    randomWeapon = random.randint(1,45)
    if randomWeapon <= 25:
        found_item = Item("Träsvärd", random.randint(15,25))
    elif randomWeapon <= 40:
        found_item = Item("Järnsvärd", random.randint(30,45))
    elif randomWeapon <= 45:
        found_item = Item("Guldsvärd", random.randint(50,75))

    chestScenario = random.randint(1, 3)
    print(f"\n        {doorText(doorChoice)}")
    time.sleep(SCENARIOPRINT_SPEED)
    if chestScenario == 1:
        print_list_slow([
            "\n        ***Du hittar en gammal kista dold bland ruinerna. Du öppnar den försiktigt.***",
            f"\n        ***Inuti hittar du ett {found_item.name.lower()} med {found_item.strength_bonus} styrkepoäng!***",
        ])
    elif chestScenario == 2:
        print_list_slow([
            "\n        ***När du vandrar genom skogen, upptäcker du en gömd skattkista.***",
            f"\n        ***Inuti finner du ett {found_item.name.lower()} med {found_item.strength_bonus} styrkepoäng!***"
        ])
    elif chestScenario == 3:
        print_list_slow([
            "\n        ***I distansen ser du någonting lysa.***",
            "\n        ***Du springer dit och hittar en guldig kista.***",
            f"\n        ***Bland skatten finns ett {found_item.name.lower()} med {found_item.strength_bonus} styrkepoäng!***"
        ])
    if len(player.inventory) >= 5:
        while True:
            changeWeapon = input(f"\n\n        Ditt inventory är fullt, vill du byta ut ditt sämsta vapen som har {find_weakest_item(player.inventory).strength_bonus} styrka, mot detta? (y/n)\n        ")           
            if changeWeapon.lower() == "y":
                remove_weakest_item()
                player.addItem(found_item)
                break
            elif changeWeapon.lower() == "n":
                break
            else:
                print("\n        Du måste svara y eller n")     
    else:
        player.addItem(found_item)
    clear()

def play_again(txt):
    while True:
        playAgain = input(txt)
        if playAgain.lower() == "y":
            player.reset()
            break
        elif playAgain.lower() == "n":
            exit()
        else:
            print("Du måste svara y eller n")

def main():#Huvudloopen
    if player.lvl == 10:
        print_list_slow([
            "\n\n        Du har övervunnit alla faror, besegrat skräckinjagande monster och plundrat gömda kistor.",
            "\n        Ditt mod och din skicklighet har tagit dig genom de mystiska dörrarna och överlevt det okända.",
            "\n        När du öppnar den sista dörren, strålar ljuset in och en känsla av triumf fyller ditt hjärta.",
            "\n        Plötsligt hör du en dånande röst från det förflutna, en röst som hyllar din styrka och mod.",
            "\n        \"Du, modige äventyrare, har klarat prövningarna och bevisat dig vara en sann hjälte!\"",
            "\n        Ditt namn kommer att bli känt och berättat i hela landet som den som erövrade Sagan Om Dörren.",
            "\n        Du står där, omgiven av ära och seger, redo för nya äventyr och oviss framtid.",
            "\n        Tack för att du deltog i Sagan Om Dörren!\n\n"
        ])
        play_again("        Grattis du vann! Vill du spela igen? (y/n)\n\n        ")
    elif player.hp <= 0:
        play_again("        Du dog! Vill du börja om? (y/n)\n\n        ")



    choose_action()
    
start_menu()

while True:
    main()