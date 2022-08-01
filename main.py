############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  return random.choice(cards)

again = True

while again:
  from art import logo
  print(logo)
  
  user_cards = []
  computer_cards = []
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  def calculate_score(card_list):
    score = sum(card_list)
    if len(card_list) == 2 and score == 21:
      return 0
    # if there's an Ace check if score greater than 21 and change to a 1
    if 11 in card_list:
      if score > 21:
        card_list.remove(11)
        card_list.append(1)
    return score

  
  print(f"your cards: {user_cards}")
  print(f"computer's first card: {computer_cards[0]}")
  
  # decide the game by comparing the two scores
  def compare(user, computer, userCards, computerCards):
    print(f"your hand: {userCards}")
    print(f"computer's hand: {computerCards}")
    if user == computer:
      print("It's a draw")
    elif computer == 0 or user > 21:
      print("You lost")
    elif computer > 21 or user == 0:
      print("You won")
    else:
      if user > computer:
        print("You win")
      elif computer > user:
        print("You lost")
  
  #based on the score compare the user and computer scores or ask user to draw a card 
  def check():
    # calculate scores
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    # if its a blackjack end the game and compare
    if user_score == 0 or computer_score == 0 or user_score > 21:
      compare(user_score, computer_score, user_cards, computer_cards)
    # ask user to draw card until they are satisfied with their hand
    else: 
      draw_card = input("Type 'y' to draw a card, or type 'n' to pass: ")
      if draw_card == 'n':
        while computer_score < 17:
          computer_cards.append(deal_card())
          computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)
        compare(user_score, computer_score, user_cards, computer_cards)
      else:
        user_cards.append(deal_card())
        print(f"your cards: {user_cards}")
        check()
  
  check()

  # ask to play again
  play_again = input("Type 'y' to play again, type 'n' to exit: ")
  if play_again == 'n':
    again = False
  else:
    clear()


