###  Roulette ####

import random
import time
import ipywidgets as widgets
print('\n' * 2)
print('**************************************************')
print('Welcome to the best Roulette game ever')
print('**************************************************')



def replay():
    while True:
        play = input("Do you desire to play again? Yes/No: ").upper()
        if play == 'YES' or play == 'NO':
            break
        else:
            continue
    return play

class Chips:

    def __init__(self):
        self.total = my_euros.tokens
        self.bet = 0


def display_board():
    print('#' + '        ' + 'OPTIONS TO BET' + '       ' + 'PAYOUT')
    print('---' + '   ' + '------------------' + '     ' + '---------')
    print('1'  + '       ' +  'Single number' + '         ' + '35 to 1')
    print('2'  + '       ' +  'Split  number' + '         ' + '17 to 1')
    print('3'  + '       ' + 'Street' + '                 ' + '11 to 1')
    print('4'  + '       ' + 'Corner' + '                ' + '8  to 1')
    print('5'  + '       ' + 'Six line' + '              ' + '5  to 1')
    print('6'  + '       ' + 'Basket' + '                ' + '6  to 1')
    print('7'  + '       ' + '1-18 numbers' + '          ' + '1  to 1')
    print('8' + '       ' + '19-36 numbers' + '         ' + '1  to 1')
    print('9' + '       ' +  'Red number' + '            ' + '1  to 1')
    print('10' + '      ' +  'Black number' + '          ' + '1  to 1')
    print('11' + '      ' +  'Even number' + '           ' + '1  to 1')
    print('12' + '      ' +  'Odd number' + '            ' + '1  to 1')
    print('13' + '      ' + 'First dozen (1-12)' + '    ' + '2  to 1')
    print('14' + '      ' + 'Second dozen (13-24)' + '  ' + '2  to 1')
    print('15' + '      ' + 'Third dozen (25-36)' + '   ' + '2  to 1')

def single_number(Chips):
    while True:
        try:
            number = int(input('\nWhich number would you like to bet on?: '))
        except:
            print('\nPlease introduce an integer')
            continue
        else:
            if number not in range(0,37):
                print('\nPlease stick to one of the possible bets')
                continue
            else:
                break
        break

    if random_number == number:
        Chips.total += 35 * Chips.bet
        return True
    else:
        Chips.total -= Chips.bet
        return False

def first_dozen(Chips):

    if random_number in [1,2,3,4,5,6,7,8,9,10,11,12]:
        Chips.total += 2 * Chips.bet
        return True
    else:
        Chips.total -= Chips.bet
        return False

def second_dozen(Chips):

    if random_number in [13,14,15,16,17,18,19,20,21,22,23,24]:
        Chips.total += 2 * Chips.bet
        return True
    else:
        Chips.total -= Chips.bet
        return False

def third_dozen(Chips):

    if random_number in [25,26,27,28,29,30,31,32,33,34,35,36]:
        Chips.total += 2 * Chips.bet
        return True
    else:
        Chips.total -= Chips.bet
        return False

def red_number(Chips):
    if random_number in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
        Chips.total +=  Chips.bet
        return True
    else:
        Chips.total -= Chips.bet
        return False

def black_number(Chips):
    if random_number in [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]:
        Chips.total +=  Chips.bet
        return True
    else:
        Chips.total -= Chips.bet
        return False

def even_number(Chips):
    if random_number != 0 and random_number%2 == 0:
        Chips.total +=  Chips.bet
        return True
    else:
        Chips.total -= Chips.bet
        return False

def odd_number(Chips):
    if random_number%2 != 0:
        Chips.total +=  Chips.bet
        return True
    else:
        Chips.total -= Chips.bet
        return False

def first_18(Chips):
    if random_number in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
        Chips.total +=  Chips.bet
        return True
    else:
        Chips.total -= Chips.bet
        return False

def second_18(Chips):
    if random_number in [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]:
        Chips.total +=  Chips.bet
        return True
    else:
        Chips.total -= Chips.bet
        return True

def split_number(Chips):

    split = input('\nWhich split number would you like to bet on [0-1/0-2/0-3/1-2/1-4...]?: ')

    if split == '0-1' and random_number in [0,1] or split == '0-2' and random_number in [0,2] or split == '0-3' and random_number in [0,3] or split == '1-2' and random_number in [1,2] or split == '1-4' and random_number in [1,4] or split == '2-3' and random_number in [2,3] or split == '2-5' and random_number in [2,5] or split == '3-6' and random_number in [3,6] or split == '4-5' and random_number in [4,5] or split == '4-7' and random_number in [4,7] or split == '5-8' and random_number in [5,8]:
        Chips.total +=  17*Chips.bet
        return True
    elif split == '5-6' and random_number in [5,6] or split == '6-9' and random_number in [6,9] or split == '7-10' and random_number in [7,10] or split == '7-8' and random_number in [7,8] or split == '8-11' and random_number in [8,11] or split == '8-9' and random_number in [8,9] or split == '9-12' and random_number in [9,12] or split == '10-11' and random_number in [10,11] or split == '10-13' and random_number in [10,13] or split == '11-14' and random_number in [11,14]:
        Chips.total +=  17*Chips.bet
        return True
    elif split == '11-12' and random_number in [11,12] or split == '12-15' and random_number in [12,15] or split == '13-16' and random_number in [13,16] or split == '13-14' and random_number in [13,14] or split == '14-17' and random_number in [14,17] or split == '14-15' and random_number in [14,15] or split == '15-18' and random_number in [15,18] or split == '16-17' and random_number in [16,17] or split == '16-19' and random_number in [16,19] or split == '17-20' and random_number in [17,20]:
        Chips.total +=  17*Chips.bet
        return True
    elif split == '17-18' and random_number in [17,18] or split == '18-21' and random_number in [18,21] or split == '19-22' and random_number in [19,22] or split == '19-20' and random_number in [19,20] or split == '20-23' and random_number in [20,23] or split == '20-21' and random_number in [20,21] or split == '21-24' and random_number in [21,24] or split == '22-25' and random_number in [22,25] or split == '22-23' and random_number in [22,23] or split == '23-26' and random_number in [23,26]:
        Chips.total +=  17*Chips.bet
        return True
    elif split == '23-24' and random_number in [23,24] or split == '24-27' and random_number in [24,27] or split == '25-28' and random_number in [25,28] or split == '25-26' and random_number in [25,26] or split == '26-29' and random_number in [26,29] or split == '26-27' and random_number in [26,27] or split == '27-30' and random_number in [27,30] or split == '28-31' and random_number in [28,31] or split == '28-29' and random_number in [28,29] or split == '29-32' and random_number in [29,32]:
        Chips.total +=  17*Chips.bet
        return True
    elif split == '29-30' and random_number in [29,30] or split == '30-33' and random_number in [30,33] or split == '31-34' and random_number in [31,34] or split == '31-32' and random_number in [31,32] or split == '32-35' and random_number in [32,35] or split == '32-33' and random_number in [32,33] or split == '33-36' and random_number in [33,36] or split == '34-35' and random_number in [34,35] or split == '35-36' and random_number in [35,36]:
        Chips.total +=  17*Chips.bet
        return True
    else:
        Chips.total -= Chips.bet
        return False


def street(Chips):
    while True:
        stre = input('\nWhich street would you like to bet on [1-3/4-6...]?: ')
        if stre != '1-3' and stre != '4-6' and stre != '7-9' and stre != '10-12' and stre != '13-15' and stre != '16-18' and stre != '19-21' and stre != '22-24' and stre != '25-27' and stre != '28-30' and stre != '31-33' and stre != '34-36':
            print('\nPlease stick to one of the possible streets')
            continue
        else:
            break

    if stre == '1-3' and random_number in [1,2,3] or stre == '4-6' and random_number in [4,5,6] or stre == '7-9' and random_number in [7,8,9] or stre == '10-12' and random_number in [10,11,12] or stre == '13-15' and random_number in [13,14,15] or stre == '16-18' and random_number in [16,17,18] or stre == '19-21' and random_number in [19,20,21] or stre == '22-24' and random_number in [22,23,24]:
        Chips.total +=  11*Chips.bet
        return True
    elif stre == '25-27' and random_number in [25,26,27] or stre == '28-30' and random_number in [28,29,30] or stre == '31-33' and random_number in [31,32,33] or stre == '34-36' and random_number in [34,35,36]:
        Chips.total +=  11*Chips.bet
        return True
    else:
        Chips.total -= Chips.bet
        return False

def corner(Chips):
    while True:
        cor = input('\nWhich corner would you like to bet on [1/2/4/5 or 2/3/5/6 or 4/5/7/8...]?: ')
        if cor!='1/2/4/5' and cor!='2/3/5/6' and cor!='4/5/7/8' and cor!='5/6/8/9' and cor!='7/8/10/11' and cor!='8/9/11/12' and cor!='10/11/13/14' and cor!='11/12/14/15' and cor!='13/14/16/17' and cor!='14/15/17/18' and cor!='16/17/19/20' and cor!='17/18/20/21' and cor!='19/20/22/23' and cor!='20/21/23/24' and cor!='22/23/25/26' and cor!='23/24/26/27' and cor!='25/26/28/29' and cor!='26/27/29/30' and cor!='28/29/31/32' and cor!='29/30/32/33' and cor!='31/32/34/35' and cor!='32/33/35/36':
            print('\nPlease stick to one of the possible streets')
            continue
        else:
            break

    if cor=='1/2/4/5' and random_number in [1,2,4,5] or cor=='2/3/5/6' and random_number in [2,3,5,6] or cor=='4/5/7/8' and random_number in [4,5,7,8] or cor=='5/6/8/9' and random_number in [5,6,8,9] or cor=='7/8/10/11' and random_number in [7,8,10,11] or cor=='8/9/11/12' and random_number in [8,9,11,12] or cor=='10/11/13/14' and random_number in [10,11,13,14] or cor=='11/12/14/15' and random_number in [11,12,14,15] or cor=='13/14/16/17' and random_number in [13,14,16,17]:
        Chips.total +=  8*Chips.bet
        return True
    elif cor=='14/15/17/18' and random_number in [14,15,17,18] or cor=='16/17/19/20' and random_number in [16,17,19,20] or cor=='17/18/20/21' and random_number in [17,18,20,21] or cor=='19/20/22/23' and random_number in [19,20,22,23] or cor=='20/21/23/24' and random_number in [20,21,23,24] or cor=='22/23/25/26' and random_number in [22,23,25,26] or cor=='23/24/26/27' and random_number in [23,24,26,27] or cor=='25/26/28/29' and random_number in [25,26,28,29]:
        Chips.total +=  8*Chips.bet
        return True
    elif cor=='26/27/29/30' and random_number in [26,27,29,30] or cor=='28/29/31/32' and random_number in [28,29,31,32] or cor=='29/30/32/33' and random_number in [29,30,32,33] or cor=='31/32/34/35' and random_number in [31,32,34,35] or cor=='32/33/35/36' and random_number in [32,33,35,36]:
        Chips.total +=  8*Chips.bet
        return True
    else:
        Chips.total -= Chips.bet
        return False

def six_line(Chips):
    while True:
        six = input('\nWhich six in line would you like to bet on [1-6/4-9/7-12...]?: ')
        if six != '1-6' and six != '4-9' and six != '7-12' and six != '10-15' and six != '13-18' and six != '16-21' and six != '19-24' and six != '22-27' and six != '25-30' and six != '28-33' and six != '31-36':
            print('\nPlease introduce a string')
            continue
        else:
            break

    if six == '1-6' and random_number in [1,2,3,4,5,6] or six == '4-9' and random_number in [4,5,6,7,8,9] or six == '7-12' and random_number in [7,8,9,10,11,12] or six == '10-15' and random_number in [10,11,12,13,14,15] or six == '13-18' and random_number in [13,14,15,16,17,18] or six == '16-21' and random_number in [16,17,18,19,20,21] or six == '19-24' and random_number in [19,20,21,22,23,24] or six == '22-27' and random_number in [22,23,24,25,26,27]:
        Chips.total +=  5*Chips.bet
        return True

    elif six == '25-30' and random_number in [25,26,27,28,29,30] or six == '28-33' and random_number in [28,29,30,31,32,33] or six == '31-36' and random_number in [31,32,33,34,35,36]:
        Chips.total +=  5*Chips.bet
        return True

    else:
        Chips.total -= Chips.bet
        return False


def basket(Chips):

    if random_number == 0 or random_number == 1 or random_number == 2 or random_number == 3:
        Chips.total +=  6*Chips.bet
        return True
    else:
        Chips.total -= Chips.bet
        return False


def roulette():
    print('\nRoulette spinning....')
    time.sleep(5)
    return random.randint(0,36)


def player_selection():
    bet_chosen = None
    while True:
        try:
            bet_chosen = int(input('\nSelect your option to bet: '))
        except:
            print('\nPlease introduce an integer')
            continue
        else:
            if bet_chosen not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
                print('\nPlease stick to one of the possible bets')
                continue
            else:
                break
        break
    return bet_chosen


def take_bet(Chips):
    betting = True
    while betting:
        try:
            Chips.bet = int(input('\nHow much you would desire to bet?: '))

        except:
            print('\nPlease introduce an intenger')
            continue
        else:
            if Chips.bet < Chips.total:
                print('\nMoney accepted')
                betting = False
            elif Chips.bet == Chips.total:
                print('\nMoney accepted. Take into account that you are betting all your money')
                while True:
                    cont = input('\nDo you want to continue? yes/no: ').upper()
                    if cont == 'YES':
                        betting = False
                        break
                    elif cont == 'NO':
                        betting = True
                        break
                    else:
                        print('\nPlease introduce one of the two aforementioned options')
                        continue
            else:
                print('\nSorry! you do not have enough funds. Bet fewer dollars!')
                continue


def display_board_odds(board):

    print('#' + '        ' + 'OPTIONS TO BET' + '       ' + 'Odds')
    print('---' + '   ' + '------------------' + '     ' + '---------')
    print('1'  + '       ' + '1-18 numbers' + '          ' + board[0])
    print('2' + '       ' + '19-36 numbers' + '         ' + board[1])
    print('3' + '       ' +  'Red number' + '            ' + board[2])
    print('4' + '       ' +  'Black number' + '          ' + board[3])
    print('5' + '       ' +  'Even number' + '           ' + board[4])
    print('6' + '       ' +  'Odd number' + '            ' + board[5])
    print('7' + '       ' + 'First dozen (1-12)' + '    ' + board[6])
    print('8' + '       ' + 'Second dozen (13-24)' + '  ' + board[7])
    print('9' + '       ' + 'Third dozen (25-36)' + '   ' + board[8])

def odds():

    if random_number == 1:
        od_num.append(random_number)
        onetoeigh.append(random_number)
        rednum.append(random_number)
        firstdozen.append(random_number)

    elif random_number == 2:
        even_num.append(random_number)
        onetoeigh.append(random_number)
        blacknum.append(random_number)
        firstdozen.append(random_number)

    elif random_number == 3:
        od_num.append(random_number)
        onetoeigh.append(random_number)
        rednum.append(random_number)
        firstdozen.append(random_number)

    elif random_number == 4:
        even_num.append(random_number)
        onetoeigh.append(random_number)
        blacknum.append(random_number)
        firstdozen.append(random_number)

    elif random_number == 5:
        od_num.append(random_number)
        onetoeigh.append(random_number)
        rednum.append(random_number)
        firstdozen.append(random_number)

    elif random_number == 6:
        even_num.append(random_number)
        onetoeigh.append(random_number)
        blacknum.append(random_number)
        firstdozen.append(random_number)

    elif random_number == 7:
        od_num.append(random_number)
        onetoeigh.append(random_number)
        rednum.append(random_number)
        firstdozen.append(random_number)

    elif random_number == 8:
        even_num.append(random_number)
        onetoeigh.append(random_number)
        blacknum.append(random_number)
        firstdozen.append(random_number)

    elif random_number == 9:
        od_num.append(random_number)
        onetoeigh.append(random_number)
        rednum.append(random_number)
        firstdozen.append(random_number)

    elif random_number == 10:
        even_num.append(random_number)
        onetoeigh.append(random_number)
        blacknum.append(random_number)
        firstdozen.append(random_number)

    elif random_number == 11:
        od_num.append(random_number)
        onetoeigh.append(random_number)
        blacknum.append(random_number)
        firstdozen.append(random_number)

    elif random_number == 12:
        even_num.append(random_number)
        onetoeigh.append(random_number)
        rednum.append(random_number)
        firstdozen.append(random_number)

    elif random_number == 13:
        od_num.append(random_number)
        onetoeigh.append(random_number)
        blacknum.append(random_number)
        secondozen.append(random_number)

    elif random_number == 14:
        even_num.append(random_number)
        onetoeigh.append(random_number)
        rednum.append(random_number)
        secondozen.append(random_number)

    elif random_number == 15:
        od_num.append(random_number)
        onetoeigh.append(random_number)
        blacknum.append(random_number)
        secondozen.append(random_number)

    elif random_number == 16:
        even_num.append(random_number)
        onetoeigh.append(random_number)
        rednum.append(random_number)
        secondozen.append(random_number)

    elif random_number == 17:
        od_num.append(random_number)
        onetoeigh.append(random_number)
        blacknum.append(random_number)
        secondozen.append(random_number)

    elif random_number == 18:
        even_num.append(random_number)
        onetoeigh.append(random_number)
        rednum.append(random_number)
        secondozen.append(random_number)

    elif random_number == 19:
        od_num.append(random_number)
        eightothirty.append(random_number)
        rednum.append(random_number)
        secondozen.append(random_number)

    elif random_number == 20:
        even_num.append(random_number)
        eightothirty.append(random_number)
        blacknum.append(random_number)
        secondozen.append(random_number)

    elif random_number == 21:
        od_num.append(random_number)
        eightothirty.append(random_number)
        rednum.append(random_number)
        secondozen.append(random_number)

    elif random_number == 22:
        even_num.append(random_number)
        eightothirty.append(random_number)
        blacknum.append(random_number)
        secondozen.append(random_number)

    elif random_number == 23:
        od_num.append(random_number)
        eightothirty.append(random_number)
        rednum.append(random_number)
        secondozen.append(random_number)

    elif random_number == 24:
        even_num.append(random_number)
        eightothirty.append(random_number)
        blacknum.append(random_number)
        secondozen.append(random_number)

    elif random_number == 25:
        od_num.append(random_number)
        eightothirty.append(random_number)
        rednum.append(random_number)
        thirdozen.append(random_number)

    elif random_number == 26:
        even_num.append(random_number)
        eightothirty.append(random_number)
        blacknum.append(random_number)
        thirdozen.append(random_number)

    elif random_number == 27:
        od_num.append(random_number)
        eightothirty.append(random_number)
        rednum.append(random_number)
        thirdozen.append(random_number)

    elif random_number == 28:
        even_num.append(random_number)
        eightothirty.append(random_number)
        blacknum.append(random_number)
        thirdozen.append(random_number)

    elif random_number == 29:
        od_num.append(random_number)
        eightothirty.append(random_number)
        blacknum.append(random_number)
        thirdozen.append(random_number)

    elif random_number == 30:
        even_num.append(random_number)
        eightothirty.append(random_number)
        rednum.append(random_number)
        thirdozen.append(random_number)

    elif random_number == 31:
        od_num.append(random_number)
        eightothirty.append(random_number)
        blacknum.append(random_number)
        thirdozen.append(random_number)

    elif random_number == 32:
        even_num.append(random_number)
        eightothirty.append(random_number)
        rednum.append(random_number)
        thirdozen.append(random_number)

    elif random_number == 33:
        od_num.append(random_number)
        eightothirty.append(random_number)
        blacknum.append(random_number)
        thirdozen.append(random_number)

    elif random_number == 34:
        even_num.append(random_number)
        eightothirty.append(random_number)
        rednum.append(random_number)
        thirdozen.append(random_number)

    elif random_number == 35:
        od_num.append(random_number)
        eightothirty.append(random_number)
        blacknum.append(random_number)
        thirdozen.append(random_number)

    elif random_number == 36:
        even_num.append(random_number)
        eightothirty.append(random_number)
        rednum.append(random_number)
        thirdozen.append(random_number)


def marking_board(board):
    board[0] = str((len(onetoeigh) / count) * 100)
    board[1] = str((len(eightothirty) / count) * 100)
    board[2] = str((len(rednum) / count) * 100)
    board[3] = str((len(blacknum) / count) * 100)
    board[4] = str((len(even_num) / count) * 100)
    board[5] = str((len(od_num) / count) * 100)
    board[6] = str((len(firstdozen) / count) * 100)
    board[7] = str((len(secondozen) / count) * 100)
    board[8] = str((len(thirdozen) / count) * 100)

gaming = True
last_numbers = []
count = 0
even_num = []
od_num = []
onetoeigh = []
eightothirty = []
rednum = []
blacknum = []
firstdozen = []
secondozen = []
thirdozen = []
the_board = [' ']*9

class Euros:

    def __init__(self):
        self.euros = euros
        self.tokens = 0

    def change_euros_to_tokens(self):
        self.tokens = self.euros * 100


while gaming:
    print('\n' * 2)
    print('Token prices\n1€ = 100 tokens')
    file = open("roulette.jpg", "rb")
    image = file.read()
    widgets.Image(value=image,format='jpg',width=300,height=400)

    while True:
        try:
            euros = float(input('\nHow many euros would you like to change: '))
        except:
            print('\nPlease introduce a floating number')
            continue
        else:
            print('\nChanging money...')
            time.sleep(5)

            my_euros = Euros()
            my_euros.change_euros_to_tokens()
            print(f'\nThere you go, you have {my_euros.tokens} tokens to play with')
            print('\n')
            time.sleep(3)
            break

    player_chips = Chips()
    still_money = True

#### latest place for listsss


    while still_money:

        print(f'Last numbers: {last_numbers}')
        print('\n')
        display_board()
        take_bet(player_chips)
        bet_chosen = player_selection()

        if bet_chosen == 1:
            random_number = roulette()
            returning = single_number(player_chips)

        elif bet_chosen == 2:
            random_number = roulette()
            returning = split_number(player_chips)


        elif bet_chosen == 3:
            random_number = roulette()
            returning = street(player_chips)

        elif bet_chosen == 4:
            random_number = roulette()
            returning = corner(player_chips)

        elif bet_chosen == 5:
            random_number = roulette()
            returning = six_line(player_chips)

        elif bet_chosen == 6:
            random_number = roulette()
            returning = basket(player_chips)

        elif bet_chosen == 7:
            random_number = roulette()
            returning = first_18(player_chips)

        elif bet_chosen == 8:
            random_number = roulette()
            returning = second_18(player_chips)

        elif bet_chosen == 9:
            random_number = roulette()
            returning = red_number(player_chips)

        elif bet_chosen == 10:
            random_number = roulette()
            returning = black_number(player_chips)

        elif bet_chosen == 11:
            random_number = roulette()
            returning = even_number(player_chips)

        elif bet_chosen == 12:
            random_number = roulette()
            returning = odd_number(player_chips)

        elif bet_chosen == 13:
            random_number = roulette()
            returning = first_dozen(player_chips)

        elif bet_chosen == 14:
            random_number = roulette()
            returning = second_dozen(player_chips)

        elif bet_chosen == 15:
            random_number = roulette()
            returning = third_dozen(player_chips)

        count += 1
        print('\nRoulette keeps spinning....')
        time.sleep(10)
        print(f'\nAnd the number is: {random_number}')

        if returning == True:
            print('\nCongratulations!')
        else:
            print('\nOhhh you lost your bet, sorry!')

        print('\n')
        print('****************************************************')
        print(f'Your funds stand at {player_chips.total} tokens')
        print('****************************************************')
        time.sleep(10)
        print('\n')
        last_numbers.append(random_number)
        odds()
        marking_board(the_board)

        if count%5 == 0:
            while True:
                want_odds = input('Do you want to check the odds? yes/no: ').upper()
                if want_odds == 'YES':
                    print('\n')
                    display_board_odds(the_board)
                    print('\n')
                    time.sleep(15)
                    while True:
                        dale = input('Do you want to continue? yes/no: ').upper()
                        print('\n')
                        if dale == 'YES':
                            break
                        elif dale == 'NO':
                            time.sleep(10)
                            continue
                        else:
                            print('\nPlease introduce one of the two aforementioned options')
                            continue
                    break

                elif want_odds == 'NO':
                    print('\n')
                    break

                else:
                    print('\nPlease introduce one of the two aforementioned options')
                    continue


        elif count%2==0:
            while True:
                give_up = input('\nDo you want to quit? yes/no: ').upper()
                if give_up == 'YES':
                    print(f'\nYou recover {player_chips.total/100}€')
                    print('\nThanks for playing')
                    print('\n')
                    still_money = False
                    gaming = False
                    break
                elif give_up == 'NO':
                    print('\n')
                    break

                else:
                    print('\nPlease introduce one of the two aforementioned options')
                    continue



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
        print('\n' * 2)
        gaming = True
    else:
        print('\n')
        print('Goodbye then')
        gaming = False
print('\n')
print('*****END*****')
