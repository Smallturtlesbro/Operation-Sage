import items.game_text


def start():
    print(items.game_text.intro_message)
    print(items.game_text.intro_q)

    while True:
        failed = "Great, now the world has been destroyed because you decided you didn't want to choose one of the " \
                 "options."
        if items.game_text.answer == "l" or items.game_text.answer == "listen":
            # if l or listen is typed for answer
            listen()
        elif items.game_text.answer == "d" or items.game_text.answer == "disregard":
            # if d or disregard is typed for answer
            disregard()
        else:
            # calls game_over() function with a "reason" argument
            game_over(failed)


# listen to the group
def disregard():
    print(items.game_text.disregard_text)

    if items.game_text.answer == "f" or items.game_text.answer == "follow":
        follow()

    elif items.game_text.answer == "s" or items.game_text.answer == "sleep":
        game_over(items.game_text.sleep)


def listen():
    print(items.game_text.listen)
    if items.game_text.answer == "c" or items.game_text.answer == "continue":
        print("hi")
    elif items.game_text.answer == "s" or items.game_text.answer == "step in":
        print("hi")
    else:
        print("hi")


def follow():
    print(items.game_text.follow)


def game_over(state):
    print(state)


start()
