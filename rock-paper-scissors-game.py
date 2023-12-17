import random

def get_choices():
    player_choice = input('Enter your choice (rock, paper or scissors): ')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {'player': player_choice, 'computer': computer_choice}
    return choices

def check_win(player, computer):
    print('You chose '+ player + ', Computer chose ' + computer)
#   print(f'You chose {player} , Computer chose {computer}')    the same strang as above, with 'f' string
    if player == computer:
        return 'It is a Tie!'
    elif player == 'rock': 
        if computer == 'scissors':
            return 'You win! Rock smashes Scissors!'
        else:
            return 'You lose! Paper covers Rock!'
    elif player == 'paper': 
        if computer == 'rock':
            return 'You win! Paper covers Rock!'
        else:
            return 'You lose! Scissors cut Paper!'
    elif player == 'scissors': 
        if computer == 'paper':
            return 'You win! Scissors cut Paper!!'
        else:
            return 'You lose! Rock smashes Scissors!'

choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)