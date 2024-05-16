# Liz Kirkwood

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)

if p1 == 'rock':
    if p2 == 'paper':
        print('Sorry, you lose')
    elif p2 == 'rock':
        print('Tied game!')
    else:
        print('You are a winner!') 
elif p1 == 'paper':
    if p2 == 'paper':
        print('Tied game!')
    elif p2 == 'rock':
        print('You are a winner!')
    else:
     print('Sorry, you lose')
else:
    if p2 == 'paper':
        print('You are a winner!')
    elif p2 == 'rock':
        print('Sorry, you lose')
    else:
     print('Tied game')      
     
     
## Using a dictionary:
       
winners = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}
p1 = random.choice(choices)
p2 = random.choice(choices)
print(f'Player 1: {p1} \n Player 2: {p2}')

if winners[p1] == p2:
    print('Player 1 wins!')
elif winners[p2] == p1:
    print('Player 2 wins!')
else:
    print('Tied game')
    
## Into a function (best option for a simple game): 
def pick_winner(p1, p2):
    if winners[p1] == p2:
        return ('Player 1 wins!')
    elif winners[p2] == p1:
        return ('Player 2 wins!')
    else:
        return ('Tied game')
    
def readysetgo():
    return random.choice(choices)
    
def one_round():
    p1 = readysetgo()
    p2 = readysetgo()
    print(f'Player 1: {p1} \n Player 2: {p2}')
    
    winner = pick_winner(p1, p2)
    print(f'The winner is...: {winner}!')
    
pick_winner(p1, p2)

## By Class

class Game():
    def __init__(self, num_players=2):
        self.choices = choices
        self.num_players = num_players
        self.players = [(n+1) for n in range(num_players)]
        
    def find_winner(self, p1, p2):
        if self.choices[p1] == p2:
            return 'Player 1'
        elif self.choices[p2] == p1:
            return 'Player 2'
        else: return 'Tie'
        
    def play_once(self):
        hands = [p.readysetgo() for p in self.players]
        print('Everyone plays:', hands)
            
        for player, hand in zip(self.players, hands):
            results = [self.find_winner(hand, h) for h in hands]
                
            wins = sum([r == 'Player 1' for r in results])
            losses = sum([r == 'Player 2' for r in results])
            ties = sum([r == 'Tie' for r in results]) - 1
            print(f'Player {player.name}: {wins} wins, {losses} losses')
            player.wins += wins

