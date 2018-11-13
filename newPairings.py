# Instantiate array of winners and losers
winners = []
losers = []

# find out when there is one winner and one loser


def placeInitialBrackets():
    # assume even number of players 0-1 / 0-5
    # 0 vs 5, 1-4, 2-3 we go up to len(numPlayers) (6)/2 - 1
    n = 0
    #     0, 1, 2         3
    while(n < len(numPlayers)/2):
        # 0, 1, 2 and 5, 4, 3
        placeBrackets(numPlayers[n],
        numPlayers[len(numPlayers)-n-1])
        n+=1
def placeBrackets(a, b):
    finalWinner = input("Who won? " + a +
                        " or " + b + "?")
    if( finalWinner == a ):
        winners.append(a)
        losers.append(b)
    else:
        winners.append(b)
        losers.append(a)
    print(winners)
    print(" are in the winners' bracket")
    print(losers)
    print(" are in the losers' bracket")

def placeLosers(a, b):
    finalWinner = input("Who won? " + a +
                        " or " + b + "?")
    if( finalWinner == a ):
        losers.remove(b)
    else:
        losers.remove(a)
    print(winners)
    print(" are in the winners' bracket")
    print(losers)
    print(" are in the losers' bracket")
# half the losers are CUT, winners stay on losers'.
def losersPlay():
    n = 0
    #     0, 1, 2         3
    while(n < len(losers)/2):
        # 0, 1, 2 and 5, 4, 3
        placeLosers(losers[n], losers[len(losers)-n-1])
        n+=1
def placeWinners(a, b):
    finalWinner = input("Who won? " + a +
                        " or " + b + "?")
    if( finalWinner == a ):
        winners.remove(b)
        losers.append(b)
    else:
        winners.remove(a)
        losers.append(a)
    print(winners)
    print(" are in the winners' bracket")
    print(losers)
    print(" are in the losers' bracket")
# half the losers are CUT, winners stay on losers'.
def winnersPlay():
    n = 0
    #     0, 1, 2         3
    while(n < len(winners)/2):
        # 0, 1, 2 and 5, 4, 3
        placeWinners(winners[n], winners[len(winners)-n-1])
        n+=1
numPlayers = input("List players based on skill, separated by spaces.").split()
print (numPlayers)
placeInitialBrackets()


# Assuming 4 players, two will be in winners' two in losers'
# After losers' player and winners' play there is one
# winner, two losers
# losers play one more time, and then winner plays loser.
while("true"):
    print(' new round')
    print(str(len(winners)) + " winners")
    print(str(len(losers)) + " losers")
    if(len(winners) == 1 and len(losers) == 1):
        # call fight, ask for winner
        finalWinner = input("Who won?")
        print (finalWinner + " wins!")
        break;
        # if one winner, but many losers, then losers must play
        # also assuming even losers
    elif(len(winners) == 1 and len(losers) != 1):
        losersPlay()
    elif(len(winners) != 1 and len(losers) == 1):
        winnersPlay()
    # if only one loser, multiple winners, then winners play only
    elif(len(winners) != 1 and len(losers) != 1):
        losersPlay()
        winnersPlay()
