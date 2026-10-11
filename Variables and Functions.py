#The rock is assigned to the player_choice using assignment oparator

player_choice = "rock"
computer_choice = "paper"


#function is a set of instructions that perform a specific task
def get_choices():
    player_choice = "rock"
    computer_choice = "paper"
    return computer_choice

#these are calling functions and storing the return values in variable
choices = get_choices()
print(choices)
