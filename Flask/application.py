from flask import Flask,render_template,request,redirect
import os
app = Flask(__name__)
app.vars = {}

app.config["CACHE_TYPE"] = "null"

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        app.vars['nPlayers'] = int(request.form['numPlayers'])
        players = app.vars['nPlayers']
        return render_template('playerNames.html', num = players )

# Instantiate array of winners and losers
allPlayers = []
winners = []
losers = []
ranking = []
winnercopy = []
losercopy = []
@app.route('/processNames', methods = ['GET', 'POST'])

def processNames():
    global allPlayers
    allPlayers = request.form.getlist('names[]')
    # assume even number of players 0-1 / 0-5
    # 0 vs 5, 1-4, 2-3 we go up to len(playerList) (6)/2 - 1
    n = 0
    #     0, 1, 2         3
    # if an odd num of players, add a 'bye'
    if(len(allPlayers) % 2 == 1):
        allPlayers.append('bye')

    #while(n < len(playerList)/2):
    #    # 0, 1, 2 and 5, 4, 3
    #    placeBrackets(playerList[n],
    #    playerList[len(playerList)-n-1])
    #    n+=1
    return redirect('/main')
# Winners' bracket, losers' bracket

# find out when there is one winner and one loser
@app.route('/main')

def main():
    global allPlayers
    global winners
    global losers

    if len(allPlayers) > 0 :
        return redirect('/initialBrackets')

    elif len(losercopy) > 1 :
        return redirect('/loserBrackets')
    elif len(winnercopy) > 1 :
        return redirect('/winnerBrackets')
    else:
        return redirect('/finalBattle')
#       Helper function for placing brackets
#
def place(winningPlayer, bracket):
    global winnercopy
    global losercopy
    global allPlayers
    global winners
    global losers
    print(" placing" + winningPlayer + " into " + bracket)
    if(bracket == "initial"):
        if(winningPlayer == "p1"):
            winners.append(allPlayers[0])
            losers.append(allPlayers[1])
        else:
            winners.append(allPlayers[1])
            losers.append(allPlayers[0])
        allPlayers.remove(allPlayers[0])
        allPlayers.remove(allPlayers[0])
    if(bracket == "winner"):
        if(winningPlayer == "p1"):
            winners.append(winnercopy[0])
            losers.append(winnercopy[1])
        else:
            winners.append(winnercopy[0])
            losers.append(winnercopy[1])
        winnercopy.remove(winnercopy[0])
        winnercopy.remove(winnercopy[0])
    if(bracket == "loser"):
        if(winningPlayer == "p1"):
            losers.append(losercopy[1])
        else:
            losers.append(losercopy[0])
        losercopy.remove(losercopy[0])
        losercopy.remove(losercopy[0])
#initial brackets
@app.route('/initialBrackets', methods = ['GET'])

def initialRound():
    global allPlayers
    p1 = allPlayers[0]
    p2 = allPlayers[1]

    return render_template('whowins.html', player1 = p1,
                brack ='/initialBrackets', player2 = p2)


@app.route('/initialBrackets', methods = ['POST'])

def placeFirst():
    place(request.form["winner"],"initial")
    if len(allPlayers) == 0 :
        global winnercopy
        global winners
        winnercopy = winners
        winners = []
    return redirect('/main')
#winners' brackets
@app.route('/winnerBrackets', methods = ['GET'])

def winnerRound():
    global winnercopy
    p1 = winnercopy[0]
    p2 = winnercopy[1]
    return render_template('whowins.html', player1 = p1,
                brack = '/winnerBrackets', player2 = p2)

@app.route('/winnerBrackets', methods = ['POST'])

def placeWinners():
    global winnercopy
    global losers
    global losercopy

    place(request.form["winner"], "winner")
    if(len(winnercopy) == 0):
        losercopy = losers
        losers = [] # move onto next round
    return redirect('/main')

#losers' bracket

@app.route('/loserBrackets', methods = ['GET'])

def loserRound():
    global losercopy
    p1 = losercopy[0]
    p2 = losercopy[1]
    return render_template('whowins.html', player1 = p1,
                brack = '/loserBrackets', player2 = p2)

@app.route('/loserBrackets', methods = ['POST'])

def placeLosers():
    global losercopy
    global winnercopy
    global winners

    place(request.form["winner"], "loser")
    if(len(losercopy) == 0 ):
        winnercopy = winners
        winners = []
    return redirect('/main')

@app.route('/finalBattle', methods = ['GET'])

def finalRound():

    return render_template('whowins.html', player1 = winners[0],
                brack = '/finalBattle', player2 = losers[0])
@app.route('/finalBattle', methods = ['POST'])

def finalPost():
    if( request.form["winner"] == "p1"):
        win = winners[0]
    else:
        win = losers[0]
    return render_template('end.html', winner = win)
if __name__ == "__main__":
    app.run(debug=True)
