import random

full_domino_set = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5],
                   [1, 6], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5],
                   [4, 6], [5, 5], [5, 6], [6, 6]]
snakes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]
stock_pieces = []
computer = []
player = []
starting_snake = []
status = ""


def deal_dominoes():
    current_set_of_dominoes = full_domino_set[:]
    stock_pieces.clear()
    computer.clear()
    player.clear()
    starting_snake.clear()
    while current_set_of_dominoes:
        stock_pieces.append(current_set_of_dominoes.pop((random.randint(0, len(current_set_of_dominoes)-1))))
        computer.append(current_set_of_dominoes.pop(random.randint(0, len(current_set_of_dominoes)-1)))
        player.append(current_set_of_dominoes.pop(random.randint(0, len(current_set_of_dominoes)-1)))
        stock_pieces.append(current_set_of_dominoes.pop(random.randint(0, len(current_set_of_dominoes)-1)))


def first_play():
    global status
    status = ""
    for snake_piece in snakes[-1:0:-1]:
        if snake_piece in computer:
            starting_snake.append(snake_piece)
            computer.remove(snake_piece)
            status = "player"
            return
        elif snake_piece in player:
            starting_snake.append(snake_piece)
            player.remove(snake_piece)
            status = "computer"
            return
        else:
            continue


def print_game():
    print(f'Stock pieces: {stock_pieces}')
    print(f'Computer pieces: {computer}')
    print(f'Player pieces: {player}')
    print(f'Domino snake: {starting_snake}')
    print(f'Status: {status}')


while True:
    deal_dominoes()
    first_play()
    print_game()
    break
