playerArray = []
currentMatches = []
num_matches = 2
winners = []
losers = []
# pairing names and their places
def dutchPairing(list_players):
    #dutch pairing
    odd = len(list_players) % 2
    if(odd == 1):
      print (list_players[-1].name + " gets a bye")
      # indices 0 1 2 3 4
      #         r c b p d
      #         len = 5
    middle = int(len(list_players) / 2)
    start = 0
    # take off the odd guy
    while(middle < len(list_players) - odd ): # 8, 9
        # first faces middle, second faces mid+1, so on.
        print (list_players[start].name + " faces " + list_players[middle].name)
        currentMatches.append(list_players[start])
        currentMatches.append(list_players[middle])
        middle+=1
        start+=1
    print ()
    print ("make sure you play in this order!")


def setWins(winner, status):
  if (winner == currentMatches[0].name):
    print(currentMatches[0].name + " wins")
    currentMatches[0].next_round("win")
    currentMatches[1].next_round("loss")
    winners.append(currentMatches[0])
    losers.append(currentMatches[1])

# if they are in the winners' bracket, loser goes to Lbracket
    if(status == "winner"):

        print(currentMatches[1].name +
        " has been moved to losers' bracket")
        winners.remove(currentMatches[1])
        losers.append(currentMatches[1]) # not sure what status they should be
    if(status == "loser"):

            print(currentMatches[1].name +
            " has been eliminated")
            losers.remove(currentMatches[1])

  else:
    print(currentMatches[1].name + " wins")

    currentMatches[1].next_round("win")
    currentMatches[0].next_round("loss")

    winners.append(currentMatches[0])
    losers.append(currentMatches[0])
    if(status == "winner"):

        print(currentMatches[0].name +
        " has been moved to losers' bracket")
        winners.remove(currentMatches[0])
        losers.append(currentMatches[0]) # not sure what status they should be

    if(status == "loser"):

            print(currentMatches[0].name +
            " has been eliminated")
            losers.remove(currentMatches[0])

  currentMatches.pop(0)
  currentMatches.pop(0)
class player:

    def __init__(self, name):
        self.name = name
        self.round = 1
        self.history = []
    def next_round(self, win_or_loss):
        self.history.append(win_or_loss)
        self.round+=1
#rich = player("rich")
#chris = player("chris")
#ben = player("ben")
#parker = player("parker")
#datian = player("datian")
#playerArray.append(rich)
#playerArray.append(chris)
#playerArray.append(ben)
#playerArray.append(parker)
#playerArray.append(datian)
#print ("round 1")
#print ()
#dutchPairing(playerArray)

#setWins("rich")

#setWins("chris")
#print()
#print("round 2")
#print()
#dutchPairing(winners)
#print()
#dutchPairing(losers)
def inputWinners(status):
    while(len(currentMatches) != 0):
        print("Who won? " + currentMatches[0].name + " or " + currentMatches[1].name + "?")
        winner = input()
        type(winner)
        setWins(winner, status)

def runTournament():
    numPlayers = input("List players based on skill, separated by spaces.").split()
    type(numPlayers)
    print()
    playerList = []
    for i in numPlayers:
        playerList.append(i)
        #print (i)
        playerArray.append(player(i))
    dutchPairing(playerArray)

    inputWinners("n/a")

    while(len(winners) > 1):
        dutchPairing(winners)
        inputWinners('winner') 
        if (len(losers) > 1):
            dutchPairing(losers)
            inputWinners('loser')
runTournament()


#print(ben.round) 2 - so you CAN pass arrays like that
