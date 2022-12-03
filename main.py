print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the treasure. Watch out for your spelling - it will literally kill you.") 
print("THE GAME BEGINS")
print("                ")
print("                ")
print("                ")

choice1 = input("You begin walking. You're in a deep forest. It is dark. It is silent. You come to a fork in the road... which way? Type left or right: \n ").lower()


if choice1 == "left":
  print("                ")
  print("                ")
  choice2 = input('Good choice. You continue walking. You hear a neigh in the distance. A green Unicorn approaches you. What do you do? Type "hello" to say hi. Type "run" to run for your life: \n').lower()
  if choice2 == "hello":   
    print("                ")
    print("                ")
    choice3 = input("You are unharmed - and you have great manners. You jump on the unicon and fly away. You arrive at 3 doors, floating in the sky. One is red, one purple, one blue. Which one do you choose? \n ").lower()
    if choice3 == "red":
      print("It's a room full of angry midgets. They smother you. GAME OVER.")
    elif choice3 == "purple":
      print("                ")
      print("                ")
      choice4 = input("You go through the purple door. THE FINAL CHALLENGE! A troll stands in front of a chest. To open it, you must answer a trivia question. He asks... \n Arachibutyrophobia is the fear of _____. a: failure b: peanut butter sticking to the roof of your mouth c: bathing \n").lower()
      if choice4 == "a":
        print("FALSE.")
      elif choice4 == "b":
        print("                ")
        print("                ")
        print("CORRECT! The troll gives you a high five and hands you the chest. YOU FOUND THE TREASURE!")
      elif choice4 == "c":
        print("FALSE.")
      else:
        print("Invalide option. You must choose a, b, or c. Dummy.")
    elif choice3 == "blue":
      print("A trap! OH NO! The door slams behind you, and the room floods with water. And piranhas. You're dead. GAME OVER.")
    else: 
      print("That door doesn't exist. Quit cheating. Now I kill you. You're dead. GAME OVER.")

  else: 
    print("Bad choice. The Unicorn is much faster and chases you down. It eats you alive. GAME OVER.")

else:
  print("You tripped on a small root, broke 7 different bones, and fractured your big toe. You're dead. GAME OVER.")
