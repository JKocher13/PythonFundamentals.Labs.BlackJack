import classes
import dealer_and_player
import typing
import time

deck = classes.Deck()


def first_deal() -> list:
    a = deck.deal()
    b = deck.deal()
    c = deck.deal()
    d = deck.deal()
    set_a = (a, c)
    set_b = (b, d)
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

def hitting(p):
    if p.score < 21:
        hs = hit_or_stand_q()
        if hs == "hit":
            a = hit_once()
            p.hit(a)
            print("Your score is " + str(player.score))
            hitting(p)
        else:
            pass
    else:
        pass

def player_moves(p):
    if p.score < 21:
        hitting(p)
        print("Your final score is " + str(p.score))
    if p.score == 21:
        print("Congrats your at 21, let\'s see what the dealer has!")


def check_for_black_jack(p, d):
    if p.score == 21:
        print("Dealers second card is " + d.cards[1].value + " of " + d.cards[1].suit)
        return False
    if d.score == 21:
        return False
    else:
        return True


def dealer_moves():
    print("Dealer\'s first card is " + dealer.cards[0].value + " of " + dealer.cards[0].suit)
    time.sleep(2)
    print("Dealer\'s first second is " + dealer.cards[1].value + " of " + dealer.cards[1].suit)
    print("Dealer\'s  score is " + str(dealer.score))
    time.sleep(2)
    while dealer.score < 17:
        print("Hit")
        time.sleep(2)
        d = hit_once()
        dealer.hit(d)
        print("Dealer\'s  score is " + str(dealer.score))
        time.sleep(2)
    print("Dealer final score is " + str(dealer.score))


def announce_deal(d, p):
    p.calc_score()
    d.calc_score()
    print("Dealer is showing " + d.cards[0].value + " of " + d.cards[0].suit)
    print("Player has\n" + p.cards[0].value + " of " + p.cards[0].suit + " and \n" +
          p.cards[1].value + " of " + p.cards[1].suit + "\nYour score is " + str(p.score))


def dealer_goes(p_score):
    if p_score > 21:
        pass
    else:
        dealer_moves()


def determine_winner(p_score, d_score):
    if p_score > 21:
        print("You went bust, you lose")
        return "Lose"
    elif p_score == d_score:
        if p_score == 21:
            print("You both hit 21! Push")
            return "Push"
        else:
            print("You both had the same score of " + str(p_score) + ". Push!")
            return "Push"
    elif d_score > 21:
        print("Dealer went bust! You win!")
        return "Win"
    elif p_score > d_score:
        print("Player wins with " + str(p_score))
        return "Win"
    elif p_score < d_score:
        print("Dealer wins with " + str(d_score))
        return "Lose"


player = dealer_and_player.Dealer_player()
dealer = dealer_and_player.Dealer_player()
x = first_deal()
player.hand(x[0][0], x[0][1])
dealer.hand(x[1][0], x[1][1])
announce_deal(dealer, player)
if check_for_black_jack(player, dealer) == True:
    player_moves(player)
    dealer_goes(player.score)
determine_winner(player.score, dealer.score)
