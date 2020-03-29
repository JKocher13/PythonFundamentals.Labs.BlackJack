import classes
import functions as fnct
import typing
import time


player = classes.Dealer_player()
dealer = classes.Dealer_player()
x = fnct.first_deal()
player.hand(x[0][0], x[0][1])
dealer.hand(x[1][0], x[1][1])
player.calc_score()
dealer.calc_score()
print("Dealer is showing " + dealer.cards[0].value + " of " + dealer.cards[0].suit)
print("Player has\n" + player.cards[0].value + " of " + player.cards[0].suit + " and \n" +
      player.cards[1].value + " of " + player.cards[1].suit + "\nYour score is " + str(player.score))
if fnct.check_for_black_jack(player, dealer) == True:
    fnct.player_moves(player)
    x = fnct.dealer_goes(player.score, dealer)
    if x is not None:
        fnct.dealer_moves(x,player)
winner_loser = fnct.determine_winner(player.score, dealer.score)
print (winner_loser)