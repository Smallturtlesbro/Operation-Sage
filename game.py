import items.game_text as gt


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
