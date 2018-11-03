import random

def input_human_play(input=input):
    play = input('rock, paper, or scissors?')
    while not is_valid_play(play):
        play = input('rock, paper, or scissors?')
    return play

def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']

def generate_computer_play():
    return random.choice(['rock', 'paper', 'scissors'])

def evaluate_game(human, computer):
        if human == computer:
            return 'tie'
        elif human == 'rock':
            if computer == 'paper':
                return 'computer'
            else:
                return 'human'
        elif human == 'paper':
            if computer == 'scissors':
                return 'computer'
            else:
                return 'human'
        else:
            if computer == 'rock':
                return 'computer'
            else:
                return 'human'



def main(input=input):
    human = input_human_play(input)
    computer = generate_computer_play()

    """
    human = input('rock, paper, or scissors?')

    while human not in ['rock', 'paper', 'scissors']:
        human = input('rock, paper, or scissors?')

    computer = random.choice(['rock', 'paper', 'scissors'])
    """
    print(computer)
    game = evaluate_game(human, computer)
    if game == 'tie':
        print('It\'s a tie')
    else:
        print(f'{game} won')


if __name__ == '__main__':
    main()


"""
elif (human == 'rock' and computer == 'scissors') or (human == 'paper' and computer == 'rock') or (human == 'scissors' and computer == 'paper'):
    print('You won.')
elif (human == 'rock' and computer == 'paper') or (human == 'paper' and computer == 'scissors') or (human == 'scissors' and computer == 'rock'):
    print('Computer won.')
else:
    print('I don\'t understand.')
"""
