# basic for loop print 0 through 9
# for i in range (10):
#     print('I is now {}'.format(i))

#simple while loop
#Condition must be initialized
# i=0
# while i < 10:
#     print('I is now {}'.format(i))
#     #increment i by 1
#     i += 1

# available_exits = ['north', 'north east', 'south']
#
# chosen_exit = ''
# while chosen_exit not in available_exits:
#     chosen_exit = input('Please choose a direction')
#     if chosen_exit == 'quit':
#         print('Game Over')
#         break
# else:
#     print('Glad you are out of there?')

#challenge
#modify the code to allow as many guesses as necessary
#Let the player whether to guess higher or lower
#print a message when correct
#optional - allow the player to quit when 0 is entered

import random

highest = 10
answer = random.randint(1, highest)
player_correct = 0
guess_number = 0

print('please guess a number between 1 and {}: '.format(highest))

while player_correct != 1:
    guess = int(input())
    if guess == 0:
        print('Goodbye')
        break
    elif guess_number == 0 and guess == answer:
        print('You got it first time')
        player_correct = 1
    elif guess < answer:
        print ('please guess higher')
        guess_number += 1
    elif guess > answer:
        print ('please guess lower')
        guess_number += 1
    else:
        player_correct = 1
        print('Awesome')
