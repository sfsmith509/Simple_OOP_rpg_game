from character import Enemy
from character import Friend
from room import Room
from item import Item


kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
kitchen.get_description()
#kitchen.describe()

dining_hall = Room("Dining Hall")
dining_hall.set_description("An exquisite room with a large long table in the middle.")
dining_hall.get_description()
#dining_hall.describe()

ballroom = Room("Ballroom")
ballroom.set_description("An abandonded and dusty room which appears to be empty.")
ballroom.get_description()
#ballroom.describe()

armory = Room("Armory")
armory.set_description("A small room containing shiny objects and a suit of armour in the corner.")
armory.get_description()

library = Room("Library")
library.set_description("A massive room the walls are covered with shelves filled with books.")
library.get_description()

## linking rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
dining_hall.link_room(library, "south")
ballroom.link_room(dining_hall, "east")
ballroom.link_room(armory, "south")
armory.link_room(ballroom, "north")
armory.link_room(library, "east")
library.link_room(dining_hall, "north")
library.link_room(armory, "west")

dave = Enemy("Dave", "A smelly zombie")
dave.get_name()
dave.set_weakness("sword")
dave.set_conversation("I want to eat your brainsss")
dining_hall.set_character(dave)

bob = Enemy("Bob", "A scary zombie")
bob.get_name()
bob.set_weakness("sword")
bob.set_conversation("mmmm delicious brainsss")
library.set_character(bob)

dora = Friend("Dora", "A friendly ghost")
dora.set_conversation("Hellooooo, I heard swords will defeat the zombies")
dora.get_name()
#dora.hug()
ballroom.set_character(dora)

sword = Item("sword")
sword.set_description("A very shiny sword")
sword.get_description()
armory.set_item(sword)
#sword.describe()

cheese = Item("cheese")
cheese.set_description("A delicious looking block of cheese")
cheese.get_description()
kitchen.set_item(cheese)

book = Item("book")
book.set_description("An old book full of spells")
book.get_description()
library.set_item(book)

candle = Item("candle")
candle.set_description("A half used long candle")
candle.get_description()
ballroom.set_item(candle)

current_room = kitchen
dead = False

backpack = []

enemies = 0


print("GAME INSTRUCTIONS")
print("To move around rooms type north, south, east or west")
print("To check if someone is in the room type talk?")                                                                         
print("To check if an item is in the room type look?")

while dead == False:		
    print("\n")         
    current_room.get_details()         
    inhabitant  = current_room.get_character()
    item_inroom = current_room.get_item()
    
    #print("Do you want to move (north, south, east or west)?")
    #print("Check if someone is in the room type talk?") #or fight? ")
    #print("Check an item is in the room type look?")
    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
#    elif command == 'check item'
    elif command == 'look':
        if item_inroom is not None:
            print('You have found an item it is a ' + item_inroom.get_name())
            item_inroom.describe()
            d = input('Do you want to take item? (y/n) ')
            if d == 'y':
                #add item to backpack
                backpack.append(item_inroom)
                print(item_inroom.get_name() + ' has been added to backpack')
            else:
                print(item_inroom.get_name() + ' has been left in ' + current_room.get_name())    
        else:
            print('No items in this room')
        
    elif command == 'talk':
        if inhabitant is not None:
            inhabitant.describe()
            a = input("Do you want to talk to " + inhabitant.get_name() + " (y/n) :")
            if a == 'y':
                input("What do you want to say? ")
                inhabitant.talk()                
                if isinstance(inhabitant, Enemy):
                    b = input("Do you want to fight with " + inhabitant.get_name() + "? (y/n) :")
                    if b == 'y':
                        print("What will you fight with? Choose item from backpack.")
                        for item in backpack:
                            print(item.get_name())
                        fight_with = input()
                        for i in backpack:
                            if fight_with == i.get_name():
#                        if fight_with in backpack:
                                print("You are using the " + fight_with + " to fight " + inhabitant.get_name())
                                if inhabitant.fight(fight_with) == True:
                                    print("You won the fight.")
                                    dead = False
                                    current_room.character = None
                                    if inhabitant.get_enemies_defeated() == 2:
                                        print("You defeated both zombies and finished the game")
                                        dead = True
                                else:
                                    print("You lost the fight.")
                                    print("GAME OVER!!!")
                                    dead = True
                            else:
                                print(fight_with + ' is not in backpack.')
                    else:
                        print("Might be best to leave then!") 

                else:
                    c = input("Do you want to thank " + inhabitant.get_name() + " for the info, with a hug? (y/n) :")
                    if c == 'y':
                        inhabitant.hug()
                        print("You are welcome")
                    else:
                        print("What ever")
            else:
                print(inhabitant.get_name() + " doesn't want to talk to you either.")
        else:
            print("No one here to talk to.")

    elif command == 'exit':
        dead = True

    else:
        print("Choose a command, 'north', 'south', 'east', 'west', 'talk', 'look', 'exit'")
