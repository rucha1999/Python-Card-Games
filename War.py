import random

def create_deck():
    """Create a deck of cards."""
    ranks = [str(num) for num in range(2, 11)] + ['J', 'Q', 'K', 'A']
    suits = ['♠', '♡', '♢', '♣']
    deck = [rank + suit for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def play_war():
    print("Let's play War!\n")
    
    deck = create_deck()
    
    player1_deck = deck[:26]
    player2_deck = deck[26:]
    
    while len(player1_deck) > 0 and len(player2_deck) > 0:
        input("Press Enter to play a card...\n")
        
        player1_card = player1_deck.pop(0)
        player2_card = player2_deck.pop(0)
        
        print(f"Player 1 plays {player1_card}")
        print(f"Player 2 plays {player2_card}\n")
        
        if player1_card[:-1] > player2_card[:-1]:
            print("Player 1 wins the round!")
            player1_deck.extend([player1_card, player2_card])
        elif player2_card[:-1] > player1_card[:-1]:
            print("Player 2 wins the round!")
            player2_deck.extend([player1_card, player2_card])
        else:
            print("It's a tie! Let's go to war...\n")
            war_cards = [player1_card, player2_card]
            
            while len(player1_deck) > 0 and len(player2_deck) > 0:
                input("Press Enter to play a card...\n")
                
                for _ in range(3):
                    if len(player1_deck) > 0 and len(player2_deck) > 0:
                        war_cards.append(player1_deck.pop(0))
                        war_cards.append(player2_deck.pop(0))
                
                print(f"Player 1 plays {war_cards[-2]}")
                print(f"Player 2 plays {war_cards[-1]}\n")
                
                if war_cards[-2][:-1] > war_cards[-1][:-1]:
                    print("Player 1 wins the war!")
                    player1_deck.extend(war_cards)
                    break
                elif war_cards[-1][:-1] > war_cards[-2][:-1]:
                    print("Player 2 wins the war!")
                    player2_deck.extend(war_cards)
                    break
                else:
                    print("Another tie! Let's go to war again...\n")
            
            if len(player1_deck) == 0:
                print("Player 2 wins the game!")
            elif len(player2_deck) == 0:
                print("Player 1 wins the game!")
    
    print("Thanks for playing!")
    
# Start the game
play_war()
