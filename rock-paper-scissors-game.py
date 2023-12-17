# import Libraries, Lists or Methods, usually import happens in the beginning of the file
import random

# variables & functions - is the peace of code which runs only if it was called, we define the function with 'def'
# 'inputs' help you to interract with the user

def get_choices():
    player_choice = input('Enter your choice (rock, paper or scissors): ')
    computer_choice = 'paper'
    choices = {'player': player_choice, 'computer': computer_choice}

    return choices