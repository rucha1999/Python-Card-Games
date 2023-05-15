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
    print("Let's play Joker!\n")
    
    deck = create_deck()

    player_hand = deck[:7]
    computer_hand = deck[7:14]
    
    print("Player's hand:", player_hand)
    
    while True:
        print("\nComputer's turn...")
        input("Press Enter to continue...")
        
        computer_card = random.choice(computer_hand)
        print("Computer plays", computer_card)
        computer_hand.remove(computer_card)
        
        if computer_card == 'Joker':
            print("Computer wins!")
            break
        
        input("\nPlayer's turn... Press Enter to play a card...")
        
        player_card = random.choice(player_hand)
        print("Player plays", player_card)
        player_hand.remove(player_card)
        
        if player_card == 'Joker':
            print("Player wins!")
            break
        
        if player_card[:-1] > computer_card[:-1]:
            print("Player wins the round!")
            player_hand.extend([player_card, computer_card])
        elif computer_card[:-1] > player_card[:-1]:
            print("Computer wins the round!")
            computer_hand.extend([player_card, computer_card])
        else:
            print("It's a tie!")
        
        print("\nPlayer's hand:", player_hand)
        print("Computer's hand:", computer_hand)
        
        if len(player_hand) == 0:
            print("Player has no cards left. Computer wins!")
            break
        elif len(computer_hand) == 0:
            print("Computer has no cards left. Player wins!")
            break
    
    print("\nThanks for playing Joker!")

# Start the game
play_joker()
