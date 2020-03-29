import classes
import time

deck = classes.Deck()


def first_deal() -> list:
    # This function picks out 4 random cards for Deck class and puts them in two sets and returns the two sets as a list
    # This function serves as a original deal to two players
    a = deck.deal()
    b = deck.deal()
    c = deck.deal()
    d = deck.deal()
    set_a = (a, c)
    set_b = (b, d)
    lst = [set_a, set_b]
    return lst


def hit_or_stand_q() -> str:
    # This function works as a repeating question until they supply either hit or stand
    x = input("Hit or Stand\n").lower()
    if x == "hit":
        return x
    elif x == "stand":
        return x
    else:
        print("Try again")
        hit_or_stand_q()


def hitting(p):
    # This functions serves as a loop that allows the player to hit if there score is less then 21
    # If they hit it allows to hit again as long as their score is over 21. This pattern stops if the player chooses
    # to stand or and then returns their score
    if p.score < 21:
        hs = hit_or_stand_q()
        if hs == "hit":
            a = deck.deal()
            p.hit(a)
            print("Your score is " + str(p.score))
            player_moves(p)


def player_moves(p: object) -> str:
    # This function is invoked when the player is done hitting and checks to see if the players score is at 21 or under
    # If the player is over 21  then this function does nothing and is skipped over
    # This function takes one variable (p) which should be an object of the Dealer_player class
    if p.score < 21:
        hitting(p)
        return "Your final score is " + str(p.score)
    if p.score == 21:
        return "Congrats your at 21, let\'s see what the dealer has!"


def check_for_black_jack(p: object, d: object) -> bool:
    # Takes in two objects and check if their variable, score, is equal to 21 if they are it returns false
    # if neither is 21 then it returns true
    if p.score == 21:
        print("Dealers second card is " + d.cards[1].value + " of " + d.cards[1].suit)
        return False
    elif d.score == 21:
        return False
    else:
        return True


def dealer_moves(d: object, p: object) -> int:
    # This function takes two objects and prints in detail the first objects cards after initial deal
    # Then it sees if the first objects score is less then 17, if so it performs a hit sequence until the score is
    # over 17 or above the players score and when the sequence is done it returns the score of the first object
    print("Dealer\'s first card is " + d.cards[0].value + " of " + d.cards[0].suit)
    time.sleep(2)
    print("Dealer\'s first second is " + d.cards[1].value + " of " + d.cards[1].suit)
    print("Dealer\'s  score is " + str(d.score))
    time.sleep(2)
    while d.score < 17 and d.score < p.score:
        print("Hit")
        time.sleep(2)
        a = deck.deal()
        d.hit(a)
        print("Dealer\'s  score is " + str(d.score))
        time.sleep(2)
    print("Dealer final score is " + str(d.score))
    return d.score


def dealer_goes(p_score: int, d: object):
    # This function determines if the dealer even needs to go. if p_score is over 21 it returns pass which skips over
    # The dealer moves function
    if p_score > 21:
        pass
    else:
        return d


def determine_winner(p_score: int, d_score: int):
    # This function determines who wins in black jack
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
        return "Dealer wins with " + str(d_score)

