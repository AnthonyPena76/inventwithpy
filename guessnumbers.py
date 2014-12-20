#guess numbers
import random

guessesTaken = 0

print ('Hey what is your name?')
myName = input()

number = random.randint(1, 200)
print ('Well, ' + myName + ', I am thinking of a number between 1 and 200. How many guesses do you need?')
guessesWanted = int(input())
while guessesTaken < guessesWanted:
    guessesWantedint = guessesWanted - guessesTaken
    guessesLeft = str(guessesWantedint)
    if guessesWantedint > 1:
        print ('Take a guess. You have ' + guessesLeft + ' guesses left.' )
    else:
        print ('Take a guess. You have ' + guessesLeft + ' guess left.' )
        
    
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print ('Your guess is too low.')
    if guess > number:
        print ('Your guess is too high.')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print ('Good job ' + myName + '! You did guessed it in only '+ guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print ('You are out of guesses. The number I was thinking of was ' + number)
