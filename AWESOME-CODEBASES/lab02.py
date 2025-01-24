# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

diceOptions = list(range(1, 7))
combatStrength = int(input("Enter your combat Strength: "))
mCombatStrength = int(input("Enter the monster's combat Strength: "))
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Health Points
input("Roll the dice for your health points (Press enter)")
healthPoints = random.choice(diceOptions)
print("You rolled " + str(healthPoints) + " health points")

input("Roll the dice for the monster's health points (Press enter)")
mHealthPoints = random.choice(diceOptions)
print("You rolled " + str(mHealthPoints) + " health points for the monster")

# Healing Potion
input("Roll the dice to see if you find a healing potion (Press enter)")
healingPotion = random.choice([0, 1])
print("Have you found a healing potion?: " + str(bool(healingPotion)))

# Weapon Select
input("Roll the dice to select your weapon (Press enter)")
numWeapons = len(weapons)
weaponRoll = random.choice(diceOptions)
print("\nYou rolled a " + str(weaponRoll))
print("You pull out a mighty " + weapons[(int(weaponRoll)-1)] + "\n")





# Analyze the Roll
input("Analyze the roll (Press enter)")
# Equality operators
print("\n--- You are matched in strength: " + str(combatStrength == mCombatStrength))

# Relational operators
print("\n--- You have a strong player: " + str((combatStrength + healthPoints) >= 15))

# and keyword
print("\n--- Remember to take a healing potion!: " + str(healingPotion == 1 and healthPoints <= 6))

# not keyword
print("\n--- Phew, you have a healing potion: " + str(
    not (                               # monster will NOT kill hero in one blow
        healthPoints < mCombatStrength  # monster will kill hero in one blow
    )
    and
    healingPotion == 1                  # hero has a healing potion
))

# or keyword
print("\n--- Things are getting dangerous: " + str(healingPotion == 0 or healthPoints == 1))

# in keyword
print("\n--- Is it possible to roll 0 in the dice?: " + str(0 in diceOptions))

# --- Expanded if statement
if healthPoints >= 5:
    print("\n--- Your health is ok")
elif healingPotion == 1:
    healingPotion = 0
    healthPoints = 6
    print("\n--- Using your healing potion... Your Health Points is now full at " + str(healthPoints))
else:
    print("\n--- Your health is low at " + str(healthPoints) + " and you have no healing potions available!")


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
