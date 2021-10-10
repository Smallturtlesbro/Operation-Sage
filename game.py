import items.game_text as gt
import items.objects as item


def prison_cell():
    inventory = ['Bread']
    print("Escape from the cell!")
    while True:
        action_input = get_player_command()
        if action_input in ['b', 'B']:
            print("You walk over to the bed.")
        elif action_input in ['c', 'C']:
            print("You walk over to your chamber pot.")
        elif action_input in ['p', 'P']:
            print("you walk to your plate and cup.")
        elif action_input in ['w', 'W']:
            print("you walk over to the cellar window.")
        elif action_input in ['i', 'I']:
            print("Inventory:")
            for item in inventory:
                print('* ' + str(item))
        else:
            print("Invalid action!")


def get_player_command():
    return input('Action: ')

def most_powerful_weapon(inventory):
    max_damage = 0
    best_weapon = None
    for item in inventory:
        try:
            if item.damage > max_damage:
                best_weapon = item
                max_damage = item.damage
        except AttributeError:
            pass
    return best_weapon


prison_cell()


'''
def start():
    print(gt.intro_message)


    while True:
        answer = input("\nWhat should I do?\n>").lower().strip()

        failed = "Great, now the world has been destroyed because you decided you didn't want to choose one of the " \
                 "options."

        if answer == 'disregard' or answer == 'd':
            # if d or disregard is typed for answer
            disregard()
        elif answer == 'exit' or answer == 'e':
            if exit_game(input, "Goodbye.", "") == True:
                break
        elif answer == 'eavesdrop' or answer == 'ev':
            eavesdrop()
        elif answer == 'help' or answer == 'h':
            print("Options: option (shortcut)")
            for option in gt.options:
                print(f'\t{option}')
        elif answer == 'investigate' or answer == 'iv':
            investigate()
        elif answer == 'listen' or answer == 'l':
            # if l or listen is typed for answer
            listen()
        elif answer == 'sleep' or answer == 's':
            if sleep(input, gt.intro_message, "") == True:
                return
        else:
            print("Invalid Option.\n Hint: type 'help' or 'h' for available options.")


# listen to the group
def disregard():
    print(gt.options["disregard (d)"])


def exit_game(input, if_yes, if_no):
    input = input("Do you want to exit? (y/n)\n>").lower()
    if input == "y":
        print(if_yes)
        return True
    else:
        print(if_no)
        return False

def eavesdrop():
    print (gt.options["listen more (lm)"])


def follow():
    print(gt.options["follow (f)"])


def investigate():
    print(gt.options["investigate (iv)"])


def game_over(state):
    print(state)


def listen():
    print(gt.options["listen (l)"])


def listen_more():
    print(gt.options["listen more (lm)"])


def sleep(input, if_yes, if_no):
    print(gt.options["sleep (s)"])
    input = input("would you like to restart?(y/n)\n>").lower()
    if input == "y":
        print(if_yes)
        return not True
    else:
        print(if_no)
        return not False


start()
'''