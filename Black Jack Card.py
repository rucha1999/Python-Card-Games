import random

def create_deck():
    suits = ['♠', '♡', '♢', '♣']

    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
    deck = [rank + suit for rank in ranks for suit in suits]

    random.shuffle(deck)

    return deck

def deal_card(deck, hand):
    """Deal a card from the deck to the player's hand."""
    card = deck.pop()
    hand.append(card)

def calculate_score(hand):
    """Calculate the score based on the hand of cards."""
    score = 0
    aces_count = hand.count('A')
    
    for card in hand:
        rank = card[:-1]
        if rank.isdigit():
            score += int(rank)
        elif rank in ('J', 'Q', 'K'):
            score += 10
    
    for _ in range(aces_count):
        if score + 11 <= 21:
            score += 11
        else:
            score += 1
    
    return score

def blackjack():
    print("Let's play Blackjack!")
    
    deck = create_deck()
    player_hand = []
    dealer_hand = []
    
    for _ in range(2):
        deal_card(deck, player_hand)
        deal_card(deck, dealer_hand)
    
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    
    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_hand[0]}")
    
    game_over = False
    
    while not game_over:
        if player_score == 21 or dealer_score == 21:
            game_over = True
        else:
            user_choice = input("Type 'y' to get another card, or 'n' to pass: ")
            
            if user_choice == 'y':
                deal_card(deck, player_hand)
                player_score = calculate_score(player_hand)
                print(f"Your cards: {player_hand}, current score: {player_score}")
                
                if player_score > 21:
                    game_over = True
            else:
                game_over = True
    
    while dealer_score < 17 and dealer_score <= player_score and player_score <= 21:
        deal_card(deck, dealer_hand)
        dealer_score = calculate_score(dealer_hand)
    
    print(f"\nYour final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    
    if player_score > 21:
        print("You went over 21. You lose!")
    elif dealer_score > 21:
        print("Dealer went over 21. You win!")
    elif player_score == dealer_score:
        print("It's a draw!")
    elif player_score > dealer_score:
        print("You win!")
    else:
        print("You lose!")

# Start the game
blackjack()
