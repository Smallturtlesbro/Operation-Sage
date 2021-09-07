'''intro_message = It's a cold windy night with no clouds. You walk into a building called
The Howling Serpent Inn. You sit down and the bartender hands you the normal order, a 
fine Elven brew called Evermead. You go to sit at a table when you hear a small group 
of three trying to keep their voices lower than everyone else.

intro_q = Why are they keeping so quiet?
I could try to Listen in on their conversation, but it might be easier to just Disregard them '''
def Start():
    print("\nIt's a cold windy night with no clouds. You walk into a building called The Howling Serpent Inn.")
    print("You sit down and the bartender hands you the normal order, a fine Elven brew called Evermead.")
    print("You go to sit at a table when you hear a small group of three trying to keep their voices lower than everyone else.")
    print("\nWhy are they keeping so quiet?")
    print("I could try to Listen in on their conversation, but it might be easier to just Disregard them")

    answer = input(">").lower()

    if "l" in answer:
        # if l or listen is typed for answer
        listen()
    elif "d" in answer:
        # if d or disregard is typed for answer
        disregard()
    else:
        # calls game_over() function with a "reason" argument
        game_over("Great, now the world has been destroyed because you decided you didn't want to choose one of the options.")

#listen to the group
def listen():
    print(''' You sit at a table right behind the group. You hear some small talk about "The Grays"
 being dug up and urns being stolen from around and outside of the city.
 The Grays?
 
 Who would be digging up dead bodies? Maybe some grave robbers?
 But they said the bodies are nowhere to be found.
 Should i step in to get more information? or should i stay quiet and keep listening? ''')

def disregard():
    "h"
def game_over():
    "p"

Start()