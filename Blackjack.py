####  BLACKJACK GAME  ######

import random
print('\n' * 2)
print('**************************************************')
print('Welcome to the best Blackjack game ever players')
print('**************************************************')
print('\n' * 2)

def replay():
    while True:
        play = input("Do you desire to play again? Yes/No: ").upper()
        if play == 'YES' or play == 'NO':
            break
        else:
            continue
    return play

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        deal_card = self.deck.pop()
        return deal_card

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = 0

    def add_card(self,Card):

        self.cards.append(Card)
        self.value += values[Card.rank]
        if Card.rank == 'Ace':
            self.ace += 1

    def check_ace(self):
        while self.value > 21 and self.ace > 0:
            self.value -= 10
            self.ace -= 1

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print('****************************************************')
    print("Player's value:", player.value)
    print('****************************************************')
    print("\n")

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print('****************************************************')
    print("\nDealer's value:", dealer.value)
    print('****************************************************')
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print('****************************************************')
    print("Player's value:", player.value)
    print('****************************************************')
    print("\n")

class Chips:

    def __init__(self):
        self.bet = 0
        self.total = 200


    def win_bet(self):
        self.total += self.bet


    def lose_bet(self):
        self.total -= self.bet


def take_bet(Chips):
    while True:
        try:
            Chips.bet= int(input('How much do you want to bet?: '))

        except:
            print("Please introduce a number")
            continue
        else:

            if Chips.bet < Chips.total:
                print('Bet took into account')
                break
            elif Chips.bet == Chips.total:
                print('Bet took into account, but take note that you have bet all your money')
                break
            else:
                print('Sorry! you do not have enough funds')
                continue

def take_hit(deck,hand):

    global player_playing

    while True:
        hitting = input('Do you want to Hit or Stand player?: ').upper()
        if hitting == 'HIT':
            hand.add_card(deck.deal())
            hand.check_ace()

        elif hitting == 'STAND':
            print("It's now the turn of the dealer")
            player_playing = False

        else:
            print('Please introduce one of the two aforementioned options')
            continue

        break

def player_busts(player,dealer,Chips):
    print('*******************************************************************')
    print('Player has been busted since their card value is greater than 21')
    print('*******************************************************************')
    print('\n')
    Chips.lose_bet()

def player_won(player,dealer,Chips):
    print('****************************************************')
    print('Player has won!')
    print('****************************************************')
    Chips.win_bet()

def dealer_won(player,dealer,Chips):

    print('****************************************************')
    print('Sorry Player you lost!')
    print('****************************************************')
    Chips.lose_bet()

def dealer_busts(player,dealer,Chips):
    print('********************************************************************************')
    print('Dealer has been busted since their card value is greater than 21. Player wins!')
    print('********************************************************************************')
    print('\n')
    Chips.win_bet()



suits = ('Hearts', 'Clubs', 'Spades', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
x = 0
gaming = True
while gaming:

    still_money = True
    player_chips = Chips()
    while still_money:
        ### lets built both dealer and player hands
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.check_ace()
        player_hand.add_card(deck.deal())
        player_hand.check_ace()

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.check_ace()
        dealer_hand.add_card(deck.deal())
        dealer_hand.check_ace()

        #lets make the bets

        take_bet(player_chips)
        show_some(player_hand,dealer_hand)


        player_playing = True

        #bank = Bank(100)
        while player_playing:
            ##player turn
            take_hit(deck, player_hand)
            show_some(player_hand,dealer_hand)

            if player_hand.value > 21:
                player_busts(player_hand,dealer_hand,player_chips)

                print (f'You have lost {player_chips.bet}€')
                player_playing = False

        if player_hand.value <= 21:

            while dealer_hand.value < player_hand.value:
                dealer_hand.add_card(deck.deal())
                dealer_hand.check_ace()

            show_all(player_hand, dealer_hand)

            if player_hand.value > dealer_hand.value:
                player_won(player_hand,dealer_hand,player_chips)
                print(f'You have won {player_chips.bet}€')
                print('\n')


            elif dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
                print(f'You have won {player_chips.bet}€.')
                print('\n')


            elif player_hand.value < dealer_hand.value:
                dealer_won(player_hand,dealer_hand,player_chips)
                print(f'You have lost {player_chips.bet}€.')
                print('\n')


            else:
                print('****************************************************')
                print("The game is draw!")
                print('****************************************************')
                print('\n')

        print( f'The funds stand at {player_chips.total}€')

        if player_chips.total == 0:
            print('\nSorry but you can not bet more since you do not have enough money')
            print('****************************************************')
            print('\n'*2)
            still_money = False
            break


    if replay() == "YES":

        print('\n')
        print('Restarting the game....')
        print('\n')
        print('**********WELCOME AGAIN**********')
        print('\n' * 3)
    else:
        print('\n')
        print('Goodbye then')
        break
print('\n')
print('*****END*****')
