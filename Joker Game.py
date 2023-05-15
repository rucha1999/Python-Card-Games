import random

def create_deck():

    """   DECK OF CARDS WITH JOKER HIDDEN SOMEWHERE  """

    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    deck.append('Joker')
    
    suits = ['♠', '♡', '♢', '♣']

    deck = [rank + suit for rank in ranks for suit in suits]
   
    random.shuffle(deck)

    return deck

def play_joker():

    print("We are starting the game JOKER\n")
    
    deck = create_deck()

    player_hand = deck[:7]

    computer_hand = deck[7:14]
    
    print("Player Card:", player_hand)
    
    while True:
        print("\nTime for computer's turn")

        input("PleaseEnter to continue...")
        
        computer_card = random.choice(computer_hand)

        print("Computer played", computer_card)

        computer_hand.remove(computer_card)
        
        if computer_card == 'Joker':
            print("Computer WON!")
            break
        
        input("\n Now its Player's turn ------ Press Enter to play a card")
        
        player_card = random.choice(player_hand)

        print("Player plays", player_card)

        player_hand.remove(player_card)
        
        if player_card == 'Joker':
            print("Player wins!")
            break
        
        if player_card[:-1]>computer_card[:-1]:
            print("Player WON the round!")
            player_hand.extend([player_card, computer_card])

        elif computer_card[:-1]>player_card[:-1]:
            print("Computer WON the round!")
            computer_hand.extend([player_card, computer_card])

        else:
            print("TIEEEEE!!!")
        
        print("\nPlayer's card:", player_hand)
        print("Computer's card:", computer_hand)
        
        if len(player_hand) == 0:
            print("Player has no cards left. Computer wins!")
            break
        elif len(computer_hand) == 0:
            print("Computer has no cards left. Player wins!")
            break
    
    print("\n**********Thanks for playing Joker!**************")

# Executing the joker game function.
play_joker()
