import items.game_text as gt


def start():
    print(gt.intro_message)
    print(gt.intro_q)


    while True:
        answer = input("\nWhat should I do?\n>")

        failed = "Great, now the world has been destroyed because you decided you didn't want to choose one of the " \
                 "options."

        if answer == "l" or answer == "listen":
            # if l or listen is typed for answer
            listen()
        elif answer == "d" or answer == "disregard":
            # if d or disregard is typed for answer
            disregard()
        elif answer == "exit":
            if exit_game(input, "Goodbye.", "") == True:
                break
        elif answer == 'investigate' or answer == 'iv':
            print(gt[investigate])
        elif answer == 'help' or answer == 'h':
            print("Options:")
            for option in gt.options:
                print(f'\t{option}')
        else:
            print("Invalid Option.\n Hint: type 'help' or 'h' for available options.")


# listen to the group
def disregard():
    print(gt.options[disregard])


def listen():
    print(gt.options[listen])


def follow():
    print(gt.options[follow])


def exit_game(input, if_yes, if_no):
    input = input("Do you want to exit? (y/n)\n>").lower()
    if input == "y":
        print(if_yes)
        return True
    else:
        print(if_no)
        return False



def game_over(state):
    print(state)


start()
