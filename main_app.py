import classes
import dealer_and_player
import typing
import time

deck = classes.Deck()

def first_deal()->list:
    deck = classes.Deck()
    a = deck.deal()
    b = deck.deal()
    c = deck.deal()
    d = deck.deal()
    set_a = (a, c)
    set_b = (b , c)
    lst = [set_a, set_b]
    return lst

def hit_once():
    x = deck.deal()
    return x

def hit_or_stand_q() -> str:
    x = input().lower()
    if x == "hit" or x == "stand":
        return x
    else:
        print("What's that bub?")
        hit_or_stand_q()

def player_moves(score: int):
    
    x = ""
    if player.score < 21 or x == "stand":
        print("Would you like to Hit or Stand?")
        x = hit_or_stand_q()
        if x == "hit":
            time.sleep(1)
            a = hit_once()
            y = player.hit(a)
            player_moves(y)
        print("Your final score is " + str(player.score))
        return player.score
    if player.score == 21:
        print("Congrats your at 21, let\'s see what the dealer has!")
        return player.score
    if player.score > 21 :
        print("You went bust! You lose")
        return player.score

def check_for_black_jack(player1 , player2):
    if player2.calc_score() == 21 and player1.calc_score() == 21:
        print("Push")
        return False
    if player1.calc_score() == 21:
        print("Player has hit Black Jack!")
        return False
    if player2.calc_score() == 21:
        print("Dealer has hit Black Jack!")
        return False




playing = True
while playing == True:
    player = dealer_and_player.Dealer_player()
    dealer = dealer_and_player.Dealer_player()
    x = first_deal()
    player.hand(x[0][0],x[0][1])
    dealer.hand(x[1][0],x[1][1])
    playing = check_for_black_jack(player,dealer)
    print("Dealer is showing " + dealer.cards[0].value + " of " + dealer.cards[0].suit)
    player.calc_score()
    print("Player has\n" + player.cards[0].value + " of " + player.cards[0].suit + " and \n" +
          player.cards[1].value + " of " + player.cards[1].suit)
    player_final_score = player_moves(player.score)
    playing = False
