import itertools
import random
##create deck
suits = ['s','c','d','h']
denominations = ['A',2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K']
face_cards = []
deck_start = itertools.product(denominations,suits)
deck = [x for x in deck_start]

##deal
x=input('Would You Like to Play Blackjack?')
print()
if x == 'No':
    print('Ok, goodbye')
else: 
    y = random.sample(range(len(deck)-1),2)
    z = random.sample(range(len(deck)-1),2)
    player_hand = [''.join(map(str,deck[index])) for index in y]
    player_hand_values = []
    for item in player_hand:
        if item[0] in ['A', 'K', 'Q', 'J', '1']:
            player_hand_values.append(10)
        else:
            player_hand_values.append(int(item[0]))
    print('You have', player_hand)
    dealer_hand_values = []
    dealer_hand = [''.join(map(str,deck[index])) for index in z]
    for item in dealer_hand:
        if item[0] in ['A', 'K', 'Q', 'J', '1']:
            dealer_hand_values.append(10)
        else:
            dealer_hand_values.append(int(item[0]))
    print('The dealer has XXXXX and', dealer_hand[0])
    print()
    print('You have', sum(player_hand_values),'.')
    hit = input('Hit? ')
    while hit in ['yes', 'Yes', 'sure']:
        x1 = random.sample(range(len(deck)-1),1)
        new_card = [''.join(map(str,deck[index])) for index in x1]
        new_card_value = new_card[0]
        player_hand.append(new_card_value[0])
        if new_card_value[0] in ['A', 'K', 'Q', 'J', '1']:
            player_hand_values.append(10)
        else:
            player_hand_values.append(int(new_card_value[0]))
        print('You hit', new_card[0])
        print('You have', sum(player_hand_values))
        if sum(player_hand_values) > 21:
            print('You Bust')  
            hit = 'no'      
        else: 
            hit = input('Hit again? ')
    if hit in ['no', 'No', 'Nah']:
        while sum(dealer_hand_values) < 15:
            x2 = random.sample(range(len(deck)-1),1)
        new_card2 = [''.join(map(str,deck[index])) for index in x2]
        new_card_value2 = new_card2[0]
        dealer_hand.append(new_card_value2[0])
        if new_card_value2[0] in ['A', 'K', 'Q', 'J', '1']:
            dealer_hand_values.append(10)
        else:
            dealer_hand_values.append(int(new_card_value2[0]))
        print