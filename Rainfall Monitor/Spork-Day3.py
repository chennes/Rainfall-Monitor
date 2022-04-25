

verbs = ["go","pick", "grab", "take", "exit","quit","bye"]
exit_commands = ["exit","quit","bye"]
directions = ["north","east","south","west"]

# . - Nothing there
# _ - Blocked
world_map = [
    "________", #0
    "_......_", #1
    "_......_", #2
    "_...a.._",
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
    while True:
        command = get_user_input()
        if command is not None:
            if command[0] in exit_commands:
                break
            process_command(command)

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

def change_map_contents(row,col,new_content):
    list_of_chars = list(world_map[row])
    list_of_chars[col] = new_content
    world_map[row] = "".join(list_of_chars)

if __name__ == "__main__":
    print_intro()
    run_event_loop()