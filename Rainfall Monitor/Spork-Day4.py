
import random

verbs = ["go","pick", "grab", "take", "exit","quit","bye","attack","thwack"]
exit_commands = ["exit","quit","bye"]
directions = ["north","east","south","west"]

# . - Nothing there
# _ - Blocked
world_map = [
    "________", #0
    "_......_", #1
    "_......_", #2
    "_..ba.._",
    "_......_",
    "_......_",
    "_......_",
    "________",
    ]

inventory = []
health = 100
position = [4,4]

def print_intro():
    print (80*"X")
    print ("X   WELCOME TO SPORK!")
    print ("X")
    print ("X A choose-your-own adventure game about... something we haven't figure out yet!")
    print ("X")
    print (80*"X")
    print ("\nYou are in am empty field, with open expanse to the north, south, east, and west.\n")

def run_event_loop():
    while health > 0:
        command = get_user_input()
        if command is not None:
            if command[0] in exit_commands:
                break
            process_command(command)
    print ("\n\nGAME OVER, LOSER. YOU ARE DEAD.\n\n")

def get_user_input():
    i = input("> ").lower()
    split_command = i.split()
    if not split_command:
        print ("Please enter a command.")
    elif split_command[0] in verbs:
        return split_command
    elif i in exit_commands:
        return split_command
    else:
        print (f"I don't know how to {split_command[0]}.")
        return None

def process_command(command):
    if command[0] == "go":
        move(command[1:])
    else:
        print (f"Command {command[0]} is unimplemented")

def move(parameters):
    for parameter in parameters:
        if parameter in directions:
            move_action (parameter)
            return
    print (f"I don't know how to move ",end="")
    for parameter in parameters:
        print (parameter + " ", end="")
    print()

def move_action(direction):
    global position
    test_position = position
    if direction == "north":
        test_position[1] -= 1
    elif direction == "east":
        test_position[0] += 1
    elif direction == "south":
        test_position[1] += 1
    elif direction == "west":
        test_position[0] -= 1
    else:
        print (f"I don't know how to move to the {direction}")
        return
    row = test_position[1]
    col = test_position[0]
    char = world_map[row][col]
    if char == ".":
        print (f"You take a few steps to the {direction}")
        position = test_position
    elif char == "a":
        position = test_position
        find_sword()
    elif char == "b":
        position = test_position
        encounter_aardvark()
    elif char == "_":
        print (f"There is a giant blocking your way. They look mean. You decide not to go {direction} after all.")

# Plot point 'a'
def find_sword():
    print ("Hey look, there is a sword here. How neat!!")
    command = get_user_input()
    if command[0] in ["pick", "grab", "take"]:
        if "sword" not in command:
            print (f"I don't know how to {command[0]} that")
            return
        inventory.append("sword")
        print ("You pick up the sword. It's very sharp and dangerous. Try not to hurt yourself!")
        row = position[1]
        col = position[0]
        change_map_contents(row,col,".")
    else:
        process_command(command)

# Plot point 'b'
def encounter_aardvark():
    print("Oh no! A giant mecha-aardvark stands in your path! It is")
    print("clearly an enemy, so it's totally OK to attack it. I mean,")
    print("if you want to. If you don't, you'll just die. Which is fine.")
    enemy_health = 50
    global health
    while enemy_health > 0 and health > 0:
        command = get_user_input()
        if command[0] in ["attack","thwack"]:
            enemy_health = attack_creature(command[1:],enemy_health)
        else:
            health = 0
            print ("You are not a very good gamer. The aardvark kills you")
            print ("easily. Have a nice afterlife.")

def attack_creature(command, enemy_health):
    hit = random.randrange(1,21)

    if "sword" in command and "sword" in inventory:
        hit = hit * 10
        print (f"Good call, you hit it with your sword, dealing {hit} damage")
    elif "sword" in command:
        print ("You miserable fool, you have no sword. You lose this turn!")
        return enemy_health
    else:
        print (f"You use your puny fists to strike at the enemy, doing a meager {hit} damage")

    enemy_health = enemy_health - hit
    if enemy_health <= 0:
        print ("Yay, you beat the enemy. Good job. You'll probably die later.")
    else:
        print (f"A good hit, but the enemy still has {enemy_health} health.")
    return enemy_health

def change_map_contents(row,col,new_content):
    list_of_chars = list(world_map[row])
    list_of_chars[col] = new_content
    world_map[row] = "".join(list_of_chars)

if __name__ == "__main__":
    print_intro()
    run_event_loop()