from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]

def func1():    
    sum = 0
    split_step = [line[1].split("|") for line in [line.split(":") for line in lines]]
    formatted_cards = []
    for line in split_step:
        formatted_card = []
        for num_string in line:
            num_string = [int(num) for num in num_string.split(" ") if num != ""]
            formatted_card.append(num_string)
        formatted_cards.append(formatted_card)
    for card in formatted_cards:
        points_of_card = 0
        for number in card[1]:
            if number in card[0]:
                points_of_card += 1
        sum += 2**(points_of_card-1) if points_of_card != 0 else 0
    return sum
                


def func2():
    #TODO: finish this
    total_cards = 0
    split_step = [line[1].split("|") for line in [line.split(":") for line in lines]]
    formatted_cards = []
    for line in split_step:
        # split the line into two lists, one for the winners and one for numbers
        formatted_card = []
        for num_string in line:
            num_string = [int(num) for num in num_string.split(" ") if num != ""]
            formatted_card.append(num_string)
        formatted_cards.append(formatted_card)
    for index_card, card in enumerate(formatted_cards):
        # determine how often the card scores points
        points_of_card = 0
        for number in card[1]:
            if number in card[0]:
                points_of_card += 1
        # since the card got evaluated, increase the total_cards counter
        total_cards += 1
        for x in range(points_of_card):
            next_element = formatted_cards[index_card+x+1]
            formatted_cards.insert(index_card+x, next_element)

    return total_cards
                

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')