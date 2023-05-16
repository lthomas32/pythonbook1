import random

# DECLARE SUIT TUPLES
SUIT_TUPLES = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
RANK_TUPLES = ('ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8  # Number of cards


def getCard(deckListIn):  # method to get a card
    thisCard = deckListIn.pop()  # pops the first/top value from the variable
    return thisCard


def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # copy the object
    random.shuffle(deckListOut)  # randomly shuffles the object
    return deckListOut


def main():
    print('Welcome to Higher or Lower')
    print('You have to choose whether the next card is higher or lower than the current card.')
    print('Getting it right adds 20 points; get it wrong and you lose 15 points')
    print('You have 50 points to start\n')

    startingDeckList = [] # create a list to hold the cards
    for suit in SUIT_TUPLES:  #O(n^2) time complexity, that feels up the list.
        for index, rank in enumerate(RANK_TUPLES):
            cardDict = {'rank': rank, 'suit': suit, 'value': index + 1}
            startingDeckList.append(cardDict)

    score = 50

    choice = 'p'

    while (choice != 'q'): # this violates the solid principle but was copying and learning from the book
        print()
        gameDeckList = shuffle(startingDeckList)  # shuffles my new deck
        currentCardDict =  getCard(gameDeckList)
        currentCardRank = currentCardDict['rank']
        currentCardValue = currentCardDict['value']
        currentCardSuit = currentCardDict['suit']
        print(f'Starting card is: {currentCardRank} of {currentCardSuit}')
        print()

        for cardNumber in range(0, NCARDS):
            answer = input(f'Will the next card be higher or lower than the {currentCardRank} of {currentCardSuit}? ('
                           f'enter h or l): ')

            answer = answer.strip().casefold()
            nextCardDict = getCard(gameDeckList);
            nextCardRank = nextCardDict['rank']
            nextCardSuit = nextCardDict['suit']
            nextCardValue = nextCardDict['value']


            print(f'Next card is: {nextCardRank} of {nextCardSuit}')

            if answer == 'h':
                if nextCardValue > currentCardValue:
                    print('You got it right, it was higher')
                    score += 20
                else:
                    print('Sorry, it was not higher')
                    score -= 15
            else:
                if nextCardValue < currentCardValue:
                    print('You got it right, it was lower')
                    score += 20
                else:
                    print('Sorry, it was not lower')
                    score -= 15

            print('Your score is: ', score)
            print()

            currentCardValue = nextCardValue
            currentCardRank = nextCardRank
            currentCardSuit = nextCardSuit

        choice = input('To quit press "q" else press enter')


    print('OK bye')

if __name__ == '__main__':
    main()






