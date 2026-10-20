from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]

def func1():
    """Return the sum of the game ids where no score is higher than the maximum allowed."""
    #split each game after its corresponding id
    splitted_by_colon = [line.split(":") for line in lines]
    #split each game into its corresponding rounds
    splitted_by_semicolon = [[game.split(";") for game in lines] for lines in splitted_by_colon]
    #split each round into its corresponding scores
    splitted_by_comma = [[[round.split(",") for round in game] for game in lines] for lines in splitted_by_semicolon]
    
    sum = 0
    for game in splitted_by_comma:
        check = 0
        # get the game_id
        game_id = int(game[0][0][0].split(" ")[1])
        # get the scores
        for round in game[1]:
            for color in round:
                quantity = color.strip().split(" ")
                # check if the quantity is higher than the maximum allowed
                if quantity[1] == "red" and int(quantity[0]) > 12: check += 1 
                if quantity[1] == "green" and int(quantity[0]) > 13: check += 1 
                if quantity[1] == "blue" and int(quantity[0]) > 14: check += 1 
        # if no score is higher than the maximum allowed, add the game_id to the sum
        if check == 0:
            sum += game_id    
    return sum

def func2():
    """Return the product of the minimal required scores for each game."""
    #split each game after its corresponding id
    splitted_by_colon = [line.split(":") for line in lines]
    #split each game into its corresponding rounds
    splitted_by_semicolon = [[game.split(";") for game in lines] for lines in splitted_by_colon]
    #split each round into its corresponding scores
    splitted_by_comma = [[[round.split(",") for round in game] for game in lines] for lines in splitted_by_semicolon]
    
    sum = 0
    for game in splitted_by_comma:
        max_red, max_green, max_blue = 0, 0, 0
        # get the scores
        for round in game[1]:
            for color in round:
                quantity = color.strip().split(" ")
                # check if the quantity is higher than the maximum allowed
                if quantity[1] == "red" and int(quantity[0]) > max_red: max_red = int(quantity[0])
                if quantity[1] == "green" and int(quantity[0]) > max_green: max_green = int(quantity[0])
                if quantity[1] == "blue" and int(quantity[0]) > max_blue: max_blue = int(quantity[0])
        # if no score is higher than the maximum allowed, add the game_id to the sum
        sum += max_red * max_green * max_blue  
    return sum

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')