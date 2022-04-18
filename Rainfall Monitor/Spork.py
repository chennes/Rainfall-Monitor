

verbs = ["go"]
exit_commands = ["exit","quit","bye"]
directions = ["north","east","south","west"]

# . - Nothing there
# _ - Blocked
world_map = [
    "________",
    "_......_",
    "_......_",
    "_......_",
    "_......_",
    "_......_",
    "_......_",
    "________",
    ]

inventory = []
health = 100
position = 4,4

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
    print ("move_action is unimplemented -- how would you implement it?")


if __name__ == "__main__":
    print_intro()
    run_event_loop()