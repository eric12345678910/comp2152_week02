# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

diceOptions = list(range(1, 7))
#combatStrength = int(input("Enter your Combat Strength: (Select a number from 1-6)"))

while True:
    try:
        combatStrength = int(input("Enter your Combat Strength: (Select a number from 1-6)"))
        if combatStrength > 1 or combatStrength < 6:
            break # valid input
        else:
            print("Error: please select a valid number (1-6)")
            
    except: 
        print("error: please enter a number between 1-6")
   
mCombatStrength = int(input("Enter the monster's Combat Strength: (Select a number from 1-6)"))
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Health Points
input("\nRoll the dice for your health points (Press enter)")
healthPoints = random.choice(diceOptions)
print("You rolled " + str(healthPoints) + " health points")

input("\nRoll the dice for the monster's health points (Press enter)")
mHealthPoints = random.choice(diceOptions)
print("You rolled " + str(mHealthPoints) + " health points for the monster")

# Healing Potion
input("\nRoll the dice to see if you find a healing potion (Press enter)")
healingPotion = random.choice([0, 1])
print("Have you found a healing potion?: " + str(bool(healingPotion)))

# Weapon Select
input("\nRoll the dice to select your weapon (Press enter)")
numWeapons = len(weapons)
weaponRoll = random.choice(diceOptions)
combatStrength += int(weaponRoll)
print("You rolled a " + str(weaponRoll))
print("Your combat strength increases to " + str(combatStrength))
print("as you reveal your mighty " + weapons[(int(weaponRoll)-1)] + "\n")

if weaponRoll <= 2:
    print("You rolled a weak weapon, friend")
elif weaponRoll <= 4:
    print("Your weapon is meh")
else:
    print("Nice weapon friend.")
if weaponRoll != 1:
    print("Thank goodness you didn't roll the Fist...")







# Analyze the Roll
input("\nAnalyze the roll (Press enter)")
# Equality operators
print("--- You are matched in strength: " + str(combatStrength == mCombatStrength))

# Relational operators
print("--- You have a strong player: " + str((combatStrength + healthPoints) >= 15))

# and keyword
print("--- Remember to take a healing potion!: " + str(healingPotion == 1 and healthPoints <= 6))

# not keyword
print("--- Phew, you have a healing potion: " + str(
    not (                               # monster will NOT kill hero in one blow
        healthPoints < mCombatStrength  # monster will kill hero in one blow
    )
    and
    healingPotion == 1                  # hero has a healing potion
))

# or keyword
print("--- Things are getting dangerous: " + str(healingPotion == 0 or healthPoints == 1))

# in keyword
print("--- Is it possible to roll 0 in the dice?: " + str(0 in diceOptions))

# --- Expanded if statement
if healthPoints >= 5:
    print("--- Your health is ok")
elif healingPotion == 1:
    healingPotion = 0
    healthPoints = 6
    print("--- Using your healing potion... Your Health Points is now full at " + str(healthPoints))
else:
    print("--- Your health is low at " + str(healthPoints) + " and you have no healing potions available!")


# --- Nested if statement
print("You meet the monster. FIGHT!!")
input("You strike first (Press enter)")

print("Your sword (" + str(combatStrength) + ") ---> Monster (" + str(mHealthPoints) + ")")
if combatStrength >= mHealthPoints:
    mHealthPoints = 0
    print("You've killed the monster")
else:
    mHealthPoints -= combatStrength

    print("You've reduced the monster's health to: " + str(mHealthPoints))

    print("The monster strikes!!!")
    print("Monster's Claw (" + str(mCombatStrength) + ") ---> You (" + str(healthPoints) + ")")
    if mCombatStrength >= healthPoints:
        healthPoints = 0
        print("You're dead")
    else:
        healthPoints -= mCombatStrength
        print("The monster has reduced your health to: " + str(healthPoints))
