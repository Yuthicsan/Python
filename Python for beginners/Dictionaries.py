def get_choices():
    player_choice = "rock"
    computer_choice = "paper"
#A dictionary is a collection of key : value pairs
    choices = {"player": player_choice , "computer" : computer_choice}

    return choices

choices = get_choices()
print(choices)