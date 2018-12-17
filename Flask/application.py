from flask import Flask,render_template,request,redirect
app = Flask(__name__)
app.vars = {}

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
# Helper function for placing brackets in processNames
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

@app.route('/processNames', methods = ['GET', 'POST'])

def placeInitialBrackets():
    allPlayers = request.form.getlist('setNames')
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
    if(len(allPlayers) > 0 ):
        return redirect('/initialBrackets')
    return redirect('/initialBrackets')

@app.route('/initialBrackets', methods = ['GET','POST'])

def winners():
    if request.method == 'GET':
        if(len(allPlayers) > 0 ):
            return render_template('whowins.html', player1 = allPlayers[0],
                        brack ='/initialBrackets', player2 = allPlayers[1])
    return redirect('/main')

if __name__ == "__main__":
    app.run(debug=True)
