#Authors: Brian Phan, Kaydon Skinner
#Date: 11/02/2023
#Description: Text-based adventure game where hero can heal, fight monsters, and find their way out.
import random

import beginnerfactory
import check_input
import expertfactory
import hero
import map


def main():
  name = input("What is your name, traveler? ")
  myHero = hero.Hero(name)

  difficulty = check_input.get_int_range(
      "Difficulty: \n1. Beginner \n2. Expert\n", 1, 2)

  if difficulty == 1:
    factory = beginnerfactory.BeginnerFactory()
  else:
    factory = expertfactory.ExpertFactory()

  myMap = map.Map()
  level = 1
  quit = False
  while myHero.hp > 0 and not quit:
    print(myHero)
    #print(myHero._location)  (testing location)

    #Main menu creation
    print(myMap.show_map(myHero.location))

    print("1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit")
    menuChoice = check_input.get_int_range("Enter choice: ", 1, 5)

    move = ''
    if menuChoice == 1:
      move = myHero.go_north()
    elif menuChoice == 2:
      move = myHero.go_south()
    elif menuChoice == 3:
      move = myHero.go_east()
    elif menuChoice == 4:
      move = myHero.go_west()
    elif menuChoice == 5:
      quit = True

    if move == 'm':
      #Monster creation and conditionals

      monster = factory.create_random_enemy()
      print(f"You encounter a {monster}")
      while (myHero.hp > 0 and monster.hp > 0):
        print(f"1. Attack {monster.name} \n2. Run away")
        choice = check_input.get_int_range("Enter choice: ", 1, 2)
        if choice == 1:
          print(myHero.attack(monster))
          print(monster.attack(myHero))
          if monster.hp < 1:
            print(f"You have slain a {monster.name}")
            myMap.remove_at_loc(myHero.location)
          elif myHero.hp < 1:
            print(f"RIP {myHero.name}")
        else: 
          print("You ran away")
          menuChoice = [1, 2, 3, 4]
          random.choice(menuChoice)
          if menuChoice == 1:
            myHero.go_south()
          elif menuChoice == 2:
            myHero.go_north()
          elif menuChoice == 3:
            myHero.go_west()
          else:
            myHero.go_east()
          break

      #Moving options & results

      print()
    elif move == 'o':
      print("You cannot go that way...\n")
    elif move == 'n':
      print("There is nothing here...")
    elif move == 's':
      print("You wound back at the start of the dungeon")
    elif move == 'i':
      print("You found a Health Potion!")
      if myHero.hp == myHero.max_hp:
        print("Seems like you already have max health, you save it for later.")
      else:
        print("You drink it to restore your health.")
        myHero.heal()
        myMap.remove_at_loc(myHero.location)
    elif move == 'f':
      print(
          "Congratulations! You found the stairs to the next floor of the dungeon."
      )
      if level >= 3:
        level = 1
      else:
        level += 1
      myMap.load_map(level)

  print("Game Over")


main()
