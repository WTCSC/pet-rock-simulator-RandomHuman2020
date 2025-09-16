from random import randint

health = 15
moss = 0
density = 3
hunger = 0

dice = randint(0, 15)

name = input("Welcome to the Pet Tungsten Cube simulator. What is your cube's name?\n> ")
if name == "":
    name = "Cubulus, The Crusher of Sidewalks"
    print("You don't know? That's fine. I'll just name it for you.")
else:
    print("That's a fitting name for a cube.")

print("All you need to know about the cube is that it only eats moss.\n\n\n\n")

while health > 0 and hunger < 25:
    input(f"{name}\n--------------------\nHunger: {hunger}\nHealth: {health}\nMoss%: {moss}\nBoredom: {density}\n--------------------\n1. Feed the cube.\n2. Walk the cube.\n3. Do nothing.\n> ")
