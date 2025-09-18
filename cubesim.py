from random import randint

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

while health > 0 and hunger < 25:
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
    elif selection == 2 and dice != 5:
        print("You take the cube on a walk. Nothing eventful happens.")
        density = density - 3
        moss = moss + 1
    elif selection == 2 and dice == 5:
        print("You take the cube on a walk. It walks directly into a patch of moss and gets stuck.")
        density = density - 3
        moss = moss + 3
        health = health - 1
