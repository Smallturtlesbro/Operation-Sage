import items.game_text


def start():
    print(items.game_text.intro_message)
    print(items.game_text.intro_q)


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
        else:
            # calls game_over() function with a "reason" argument
            game_over(failed)


# listen to the group
def disregard():
    print(items.game_text.disregard_text)


def listen():
    print(items.game_text.listen)


def follow():
    print(items.game_text.follow)


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
