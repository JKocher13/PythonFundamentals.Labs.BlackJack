import classes
import functions as fnct
import typing
import time


player = classes.Dealer_player()
dealer = classes.Dealer_player()
x = fnct.first_deal()
player.hand(x[0][0], x[0][1])
dealer.hand(x[1][0], x[1][1])
fnct.announce_deal(dealer, player)
if fnct.check_for_black_jack(player, dealer) == True:
    p = fnct.player_moves(player)
    print(p)
    x = fnct.dealer_goes(player.score, dealer)
    if x is not None:
        fnct.dealer_moves(x)
winner_loser = fnct.determine_winner(player.score, dealer.score)
print (winner_loser)