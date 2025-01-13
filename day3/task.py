print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You are at the edge of a mystical forest. Do you go 'right' or 'left'? ").lower()
if choice1 == "right":
    print("🌟 You find a glowing map that reveals hidden paths!")
else:
    print("🐺 You are attacked by wolves. GAME OVER.")
    exit()

choice2 = input("The map leads you to a river. Do you want to 'swim' across or 'build' a raft? ").lower()
if choice2 == "build":
    print("🛶 You build a sturdy raft and safely cross the river!")
else:
    print("💦 You try to swim but are swept away by the current. GAME OVER.")
    exit()

choice3 = input("You spot a guard protecting the treasure cave. Do you 'fight' the guard or 'sneak' past? ").lower()
if choice3 == "sneak":
    print("🤫 You sneak past the guard unnoticed!")
else:
    print("⚔️ The guard defeats you in combat. GAME OVER.")
    exit()

choice4 = input("Inside the cave, you find two paths: one leading up and one leading down. Do you go 'up' or 'down'? ").lower()
if choice4 == "down":
    print("🔦 You find an ancient key hidden in a chest!")
else:
    print("🌀 You get lost in a maze of tunnels. GAME OVER.")
    exit()

choice5 = input("At the end of the passage, you see two doors: one with fire and the other with ice. Which door do you choose? 'fire' or 'ice': ").lower()
if choice5 == "ice":
    print("❄️ You step into a cool chamber and find the legendary treasure! 🏆")
else:
    print("🔥 You are burned by the flames. GAME OVER.")
