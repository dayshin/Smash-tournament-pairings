# Instantiate array of winners and losers
winners = ["datian"]
losers = ["rich"]

# find out when there is one winner and one loser

if(len(winners) == 1):
    # if one winner, one loser, they battle
    if(len(losers) == 1):
        # call fight, ask for winner
        finalWinner = input(Who won?)
        break;
