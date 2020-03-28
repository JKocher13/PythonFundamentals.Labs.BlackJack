import classes
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


def hit_or_stand_q() -> str:
    x = ""
    while x is not "hit" or x is not "stand":
        x = input("Pick hit or stand\n")
        return x
    return x

def hitting(p):
    if p.score < 21:
        hs = hit_or_stand_q()
        if hs == "hit":
            a = deck.deal()
            p.hit(a)
            print("Your score is " + str(p.score))
            hitting(p)
        else:
            return p.score
    else:
        return p.score

def player_moves(p):
    if p.score < 21:
        hitting(p)
        return "Your final score is " + str(p.score)
    if p.score == 21:
        return "Congrats your at 21, let\'s see what the dealer has!"


def check_for_black_jack(p, d):
    if p.score == 21:
        print("Dealers second card is " + d.cards[1].value + " of " + d.cards[1].suit)
        return False
    if d.score == 21:
        return False
    else:
        return True


def dealer_moves(d):
    print("Dealer\'s first card is " + d.cards[0].value + " of " + d.cards[0].suit)
    time.sleep(2)
    print("Dealer\'s first second is " + d.cards[1].value + " of " + d.cards[1].suit)
    print("Dealer\'s  score is " + str(d.score))
    time.sleep(2)
    while d.score < 17:
        print("Hit")
        time.sleep(2)
        a = deck.deal()
        d.hit(a)
        print("Dealer\'s  score is " + str(d.score))
        time.sleep(2)
    print("Dealer final score is " + str(d.score))


def announce_deal(d, p):
    p.calc_score()
    d.calc_score()
    print("Dealer is showing " + d.cards[0].value + " of " + d.cards[0].suit)
    print("Player has\n" + p.cards[0].value + " of " + p.cards[0].suit + " and \n" +
          p.cards[1].value + " of " + p.cards[1].suit + "\nYour score is " + str(p.score))


def dealer_goes(p_score,d):
    if p_score > 21:
        pass
    else:
        return d


def determine_winner(p_score, d_score):
    if p_score > 21:
        time.sleep(1)
        return "You went bust, you lose"
    elif p_score == d_score:
        if p_score == 21:
            time.sleep(1)
            return "You both hit 21! Push"
        else:
            time.sleep(1)
            return "You both had the same score of " + str(p_score) + " Push!"
    elif d_score > 21:
        time.sleep(1)
        return "Dealer went bust! You win!"
    elif p_score > d_score:
        time.sleep(1)
        return "Player wins with " + str(p_score)
    elif p_score < d_score:
        time.sleep(1)
        return"Dealer wins with " + str(d_score)





