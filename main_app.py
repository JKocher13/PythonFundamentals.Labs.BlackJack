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
    x = input("Would you like to hit or stand\n").lower()
    if x == "hit" or x == "stand":
        return x
    else:
        print("What's that bub?")
        hit_or_stand_q()



def player_moves():
    if player.score < 21 or x == "stand":
        x = hit_or_stand_q()
        while x == "hit":
            time.sleep(1)
            a = hit_once()
            y = player.hit(a)
            print("Your score is " + str(player.score))
            x = hit_or_stand_q()
    if player.score == 21:
        print("Congrats your at 21, let\'s see what the dealer has!")
    if player.score > 21 :
        print("You went bust! You lose")

def bust():
    if player.score > 21:
        return False

def check_for_black_jack():
    if dealer.calc_score() == 21 and player.calc_score() == 21:
        print("Push")
        return False
    if player.calc_score() == 21:
        print("Player has hit Black Jack!")
        return False
    if dealer.calc_score() == 21:
        print("Dealer has hit Black Jack!")
        return False
    else:
        return True

def dealer_moves():
    print("Dealer\'s first card is " + dealer.cards[0].value + " of " + dealer.cards[0].suit)
    time.sleep(1)
    print("Dealer\'s first second is " + dealer.cards[1].value + " of " + dealer.cards[1].suit)
    print("Dealer\'s  score is " + str(dealer.score))
    time.sleep(2)
    while dealer.score < 17:
        print("Hit")
        d = hit_once()
        dealer.hit(d)
        print("Dealer\'s  score is " + str(dealer.score))
        time.sleep(2)
    print("Dealer final score is " + str(dealer.score))

def announce_moves():
    print("Dealer is showing " + dealer.cards[0].value + " of " + dealer.cards[0].suit)
    player.calc_score()
    print("Player has\n" + player.cards[0].value + " of " + player.cards[0].suit + " and \n" +
      player.cards[1].value + " of " + player.cards[1].suit+"\nYour score is " + str(player.score))



player = dealer_and_player.Dealer_player()
dealer = dealer_and_player.Dealer_player()
x = first_deal()
player.hand(x[0][0],x[0][1])
dealer.hand(x[1][0],x[1][1])
announce_moves()
if check_for_black_jack() == True:
    player_moves()
print("Your final score is " + str(player.score))
if player.score <= 21:
    dealer_moves()
    if dealer.score >= 22:
        print("You Win!")
    elif player.score > dealer.score:
        print("You Win!")
    else:
        ("Dealer Wins!")
else:
    print("Dealer Wins!")
