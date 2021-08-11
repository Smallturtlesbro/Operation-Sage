print("Escape from the cell!")

print("you see a Bed, the Bars, a Mirror, and a Chamber pot.")

action_input = input('Action: ')

if action_input == 'Bed':
    print("You walk over to the bed.")
elif action_input == 'Mirror':
    print("You walk to the mirror.")
elif action_input == 'Chamber pot':
    print("You walk over to the chamber pot.")
elif action_input == 'Bars':
    print("You walk over to the bars.")
else:
    print("Invalid action!")
