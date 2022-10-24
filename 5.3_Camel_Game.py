'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''

# Code by Matthew A.

import os
import time
import random

# Basic stats
done = False
continueGame = False
camelMiles = 0
nativeMiles = 0
water = 100
energy = 100
canteens = 5
money = 30
speedMult = 1
days = 1
lastMove = 1
replenishedDays = 0

treasureChance = 4
treasureItems = ["Gatorade", "Raygun", "Coupon", "Piece of trash"]
userItems = []

# Upgrade Shop
canteensCost = 30
# horseShoes -- The list means [speed multiplier, price]
horseShoeNames = ["None","Bronze","Silver","Gold","Platinum","Rocket"]
horseShoes = {horseShoeNames[0]: [1,0],
              horseShoeNames[1]: [2,75],
              horseShoeNames[2]: [4,200],
              horseShoeNames[3]: [7,1500],
              horseShoeNames[4]: [20,5000],
              horseShoeNames[5]: [100,50000]}
oasisUpgradeCost = 250
treasureUpgradeCost = 400

# Upgrade Stats
horseShoeTier = 0
oasisChance = 20


def clear_screen():
    os.system('clear')

def title_screen():
    print("")


'''

def animate():
    time.sleep(0.2)
    clear_screen()
    print("  O    /)_")
    print("__(\__/_'_)")
    print("|  l  |")
    print("|     |")
    
'''

def move_natives():
    global nativeMiles, camelMiles, days
    if days < 3: return

    nativeMiles += round(random.randint(5,8) * (days/10 + 1))
    if nativeMiles >= camelMiles:
        print("! The natives have caught you!")
        camel_died()

def camel_rest():
    global energy, days
    energy = 100
    print("+ You and your camel have rested well!")
    move_natives()
    days += 1

def camel_drink(amt):
    global water, canteens
    if canteens > 0:
        water += amt
        canteens -= 1
        if water > 100:
            water = 100
        print("+ You drank your canteen! You have {} remaining!\n".format(canteens))

    else:
        print("! Your canteens have ran dry! Wait for an oasis to get more!\n")

def camel_run(speedMult, waterCost, energyCost):
    global camelMiles, water, energy, days, replenishedDays
    camelMiles += round(random.randint(5,12) * speedMult)
    water -= waterCost
    energy -= energyCost
    check_camel()
    move_natives()
    check_oasis()
    treasure_chest()
    if replenishedDays > 0: replenishedDays -= 1
    days += 1

def camel_died():
    global done, camelMiles
    done = True
    print("You made it {} miles!".format(camelMiles))
    print("Better luck next time!")
    exit()

def check_camel():  # Make sure it hasn't run out of anything
    global water, energy
    if energy <= 0:
        print("Your camel has died of exhaustion!")
        camel_died()
    elif water <= 0:
        print("Your camel has died of dehydration!")
        camel_died()

def camel_status():
    global days, camelMiles, nativeMiles, water, energy, speedMult, money
    print("\n* Days passed: {}".format(days))
    print("* Miles travelled: {}".format(camelMiles))
    print("* % of the way to the moon: {}%".format(round((camelMiles / 238900) * 100, 4)))
    print("* Native miles travelled: {}".format(nativeMiles))
    print("* Water level: {}".format(water))
    print("* Energy level: {}".format(energy))
    print("* Money: {}".format(money))
    print("* Speed multiplier: x{}".format(speedMult))
    print("* Oasis chance per turn: {}%".format(oasisChance))
    print("* Treasure chance per turn: {}%".format(treasureChance))
    print("\n")

def check_oasis():
    global canteens, oasisChance, money, days
    if random.randint(1,100) <= oasisChance:
        moneyFound = round(random.randint(15,40) * (days/10 + 1))
        print("+ You have found an oasis!\n+ You filled +3 canteens!")
        print("+ You also found ${}!\n".format(moneyFound))
        money += moneyFound
        canteens += 3

def treasure_chest():
    global userItems, treasureItems, treasureChance
    if random.randint(1,100) <= treasureChance:
        print("! You found a treasure chest alongside the road!")
        print("Open it?")
        print("Y] Yes")
        print("N] No")
        choiceInput = input("\nChoose your option: ").lower().strip()
        if choiceInput == "y" or choiceInput == "yes":
            chosenItem = treasureItems[random.randint(0, len(treasureItems)-1)]
            userItems.append(chosenItem)
            print("\n+ You found a {}!".format(chosenItem))
            print("-"*30)
        move_natives()

def use_item():
    global userItems, replenishedDays, canteensCost, treasureUpgradeCost, oasisUpgradeCost, horseShoes
    print("Type in the number to use the item")
    print("Your items:")
    count = 0
    for i in userItems:
        count += 1
        print("{}] {}".format(count, i))
    print("e] EXIT menu")
    useItemInput = input("\nChoose your option: ").lower().strip()

    if useItemInput == "e": return

    try:
        selectedItem = userItems[int(useItemInput)-1]

        if selectedItem == "Gatorade":
            print("You drank the Gatorade! Thirst and Energy replenished for +3 turns!")
            replenishedDays += 3
        elif selectedItem == "Raygun":
            if random.randint(1,10) == 1:
                print("\n"*10 + "You aimed your raygun at the natives behind you...")
                print("You fire and it incinerates them all!")
                print("You won the raygun ending!")
                win()
            else:
                print("You aimed your raygun at the natives behind you...")
                print("You try to fire it but it doesn't work. You throw it away.")
        elif selectedItem == "Coupon":
            print("You scanned the coupon! -5% discount on all upgrades!")
            canteensCost = round(canteensCost * 0.95)
            oasisUpgradeCost = round(oasisUpgradeCost * 0.95)
            treasureUpgradeCost = round(treasureUpgradeCost * 0.95)
            for item in horseShoes:
                horseShoes[item][1] = round(horseShoes[item][1] * 0.95)

        elif selectedItem == "Piece of trash":
            print("There's nothing you can do with this...")

        userItems.pop(userItems.index(selectedItem))
    except:
        print("That was not a valid list input! Try again some other time!")

def upgrade_menu():
    global horseShoeTier, horseShoes, money, speedMult, canteens, canteensCost, oasisChance, oasisUpgradeCost, treasureUpgradeCost, treasureChance

    nextShoeName = horseShoeNames[horseShoeTier + 1]
    nextShoeMult = horseShoes[horseShoeNames[horseShoeTier+1]][0]
    nextShoeCost = horseShoes[horseShoeNames[horseShoeTier+1]][1]

    print("Welcome to the upgrade shop!")
    print("You have: ${}".format(money))
    print("1] Upgrade to {} horseshoes ... ${}".format(nextShoeName, nextShoeCost))
    print("2] Buy +3 canteens ............ ${}".format(canteensCost))
    print("3] +3% Chance of oasis ....... ${}".format(oasisUpgradeCost))
    print("4] +5% Chance of treasure .... ${}".format(treasureUpgradeCost))
    print("e] EXIT menu")

    userUpgradeInput = input("\nChoose your option: ").lower().strip()

    if userUpgradeInput == "1":
        if money < nextShoeCost:
            print("You can't afford that!")
        else:
            money -= nextShoeCost
            speedMult = nextShoeMult
            horseShoeTier += 1
            print("Purchased successfully! Your speed multiplier is now x{}!".format(nextShoeMult))
    elif userUpgradeInput == "2":
        if money < canteensCost:
            print("You can't afford that!")
        else:
            money -= canteensCost
            canteens += 3
            print("Purchased successfully! You now have {} canteens!!".format(canteens))
            canteensCost += 5
    elif userUpgradeInput == "3":
        if money < oasisUpgradeCost:
            print("You can't afford that!")
        else:
            money -= oasisUpgradeCost
            oasisChance += 3
            print("Purchased successfully! Oasis chance upgraded {}% -> {}%!".format(oasisChance - 3, oasisChance))
            oasisUpgradeCost *= 2
    elif userUpgradeInput == "4":
        if money < treasureUpgradeCost:
            print("You can't afford that!")
        else:
            money -= treasureUpgradeCost
            treasureChance += 5
            print("Purchased successfully! Treasure chance upgraded {}% -> {}%!".format(treasureChance - 5, treasureChance))
            treasureUpgradeCost *= 2
    elif userUpgradeInput == "e" or userUpgradeInput == "exit":
        print("Come back another time!")
    else:
        print("That is not an available item! Come back another time!")
    print("-"*30 + "\n")

def win():
    global done, camelMiles
    done = True
    print("--- Final Stats ---")
    camel_status()
    print("\nYou win!")
    print("\nThank you for playing!")
    print("\n(Coded by Matthew Avis for CSP, 2022)")
    exit()

def ufo():
    global done, camelMiles
    done = True
    print("You and your camel begin lifting into the sky")
    print("You got abducted by a UFO")


print("Would you like instructions?")
userInput = input().lower().strip()
if userInput == "y" or userInput == "yes":
    print("Welcome to Camel 2!")
    print("The natives are after your camel!")
    print("You need to cross 100 miles to win!")
    print("But you are given the choice to continue after you win")
    print("You can continue up to 238,900 miles (the moon)")
    print("This is only possible if you buy upgrades to make your camel faster")
    print("Remember to maintain your camel's water, energy, and other stats")
    print("Water canteens can be found in an oasis or bought")
    print("There are also other hidden features too! Good luck!")
    print("By Matthew A. for CSP")

while not done:
    if random.randint(1,10000) == 1:
        ufo()

    if camelMiles >= 100 and continueGame == False:
        print("\n"*10 + "You have crossed 100 miles!")
        print("You have won the game! Congrats!")
        print("Do you want to continue to the moon?")
        print("Y] Yes")
        print("N] No")
        yesNoInput = input().strip().lower()
        if yesNoInput == "n" or yesNoInput == "no":
            print("Thanks for playing!")
            win()
        else:
            print("\n"*10 + "-"*30 + "\nThis will take a while but good luck i guess\n" + "-"*30)
            continueGame = True


    if camelMiles >= 238900:
        print("\n"*10 + "After 238900 miles...")
        print("You have won the moon ending!")
        win()

    if replenishedDays > 0:
        print("** Gatorade power-up active for {} more turns!".format(replenishedDays))
        water, energy = 100, 100
    if days >= 15 and horseShoeTier == 0: print("// WARNING // Buy an upgrade soon!")
    if water < 40: print("// WARNING // Low water!")
    if energy < 40: print("// WARNING // Low energy!")
    print("* Day {}".format(days))
    print("* You have travelled {} miles".format(camelMiles))
    if days > 2: print("* The natives are {} miles behind you".format(camelMiles-nativeMiles))
    print("* ${}".format(money))
    print("1] DRINK from your canteen")
    print("2] Ahead MODERATE SPEED")
    print("3] Ahead FULL SPEED")
    print("4] STOP for the night")
    print("5] INVENTORY")
    print("6] UPGRADE menu")
    print("7] STATUS check")
    print("8] QUIT")
    userInput = input("\nChoose your option: ").lower().strip()

    print("\n" * 10)
    print("-" * 30)

    if userInput == "1" or userInput == "drink":
        camel_drink(40)
    elif userInput == "2" or userInput == "moderate speed":
        camel_run(1 * speedMult, 20, 15)
    elif userInput == "3" or userInput == "full speed":
        camel_run(2 * speedMult, 30, 30)
    elif userInput == "4" or userInput == "stop":
        camel_rest()
    elif userInput == "5" or userInput == "inventory":
        use_item()
    elif userInput == "6" or userInput == "upgrade":
        upgrade_menu()
    elif userInput == "7" or userInput == "status":
        camel_status()
    elif userInput == "8" or userInput == "quit":
        print("You travelled {} miles that game!\nThanks for playing!".format(camelMiles))
        done = True
