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



numPlayers = input("List players based on skill, separated by spaces.").split()
print (numPlayers)
placeInitialBrackets()

while("true"):
    if(len(winners) == 1):
        # if one winner, one loser, they battle
        if(len(losers) == 1):
            # call fight, ask for winner
            finalWinner = input("Who won?")
            print (finalWinner + " wins!")
            break;
