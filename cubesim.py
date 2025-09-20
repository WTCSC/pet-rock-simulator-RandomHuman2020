from random import randint
import time

health = 15
moss = 0
density = 3
hunger = 0

name = input("Welcome to the Pet Tungsten Cube simulator. What is your cube's name?\n> ")
if name == "":
    name = "Cubulus, The Crusher of Sidewalks"
    print("You don't know? That's fine. I'll just name it for you.")
else:
    print("That's a fitting name for a cube.")

print("All you need to know about the cube is that it only eats moss.\n\n\n\n")
time.sleep(2.5)

while health > 0 and hunger < 25 and moss < 30 and density < 50:
    dice = randint(0, 15)
    selection = input(f"{name}\n--------------------\nHunger: {hunger}\nHealth: {health}\nMoss%: {moss}\nBoredom: {density}\n--------------------\n1. Feed the cube.\n2. Walk the cube.\n3. Clean the cube.\n4. Do nothing.\n> ")

    if selection == "1" and dice != 6 and hunger > 0:
        print("You place a small amount of moss on top of the cube. The cube absorbs the moss with gusto.")
        hunger = hunger - 3
    elif selection == "1" and hunger <= 0:
        print("You place a small amount of moss on top of the cube. The moss grows over the cube. Seems the cube isn't hungry right now.")
        moss = moss + 2
    elif selection == "1" and dice == 6 and hunger > 0:
        print("You place a small amount of moss on top of the cube. The cube absorbs the moss with gusto.")
        hunger = hunger - 2
        moss = moss + 1
    elif selection == "2" and dice != 5 and density <= 0:
        print("You take the cube on a walk. Nothing eventful happens.")
        moss = moss + 1
        hunger = hunger + 1
    elif selection == 2 and dice == 5 and density <= 0:
        print("You take the cube on a walk. It walks directly into a patch of moss and gets stuck.")
        moss = moss + (randint(3, 5))
        hunger = hunger + 1
    elif selection == "2" and dice != 5 and density != 0:
        print("You take the cube on a walk. Nothing eventful happens.")
        density = density - 3
        moss = moss + 1
        hunger = hunger + 1
    elif selection == "2" and dice == 5 and density != 0:
        print("You take the cube on a walk. It walks directly into a patch of moss and gets stuck.")
        density = density - 3
        moss = moss + (randint(3, 5))
        health = health - 1
        hunger = hunger + 1
    elif selection == "3" and dice != 2 and moss <= 5:
        print("You clean the cube. It gets a little shinier.")
        moss = moss - 5
        hunger = hunger + 1
        density = density + 1
    elif selection == "3" and dice != 2 and moss > 5:
        print("You clean the cube. A surprising amount of moss grew on it.")
        moss = moss - (randint(6, 10))
        hunger = hunger + 1
        density - density + 1
    elif selection == "3" and dice == 2:
        print("You attempt to clean the cube. The moss grows back faster than you can clean it off.")
        moss = moss + (randint(1, 3))
        hunger = hunger + 1
        density = density + 1
    elif selection == "3" and moss <= 0:
        print("You attempt to clean the cube. You can't tell the difference between how it looked before you cleaned it and after.")
        hunger = hunger + 1
        density = density + 1
    else:
        print("You do nothing. The cube seems bored.")
        hunger = hunger + 1
        density = density + (randint(1, 5))

    if hunger > 5 and health > 15:
        health = health + 1

if density < 50:
    print("Your tungsten cube got too bored and left. You never see it again.")
    quit()
elif moss < 30:
    print("Your tungsten cube was overtaken by the moss.")
elif hunger < 25:
    print("You neglected to feed your tungsten cube, and it was taken away by the Cube Protective Services.")
elif health >= 0:
    print("Your cube has died.")

