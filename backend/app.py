
from flask import Flask, request, jsonify
from flask_cors import CORS
from FirebaseAccess.firebase import db
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

# Initialize Firebase
load_dotenv()

# Initialize Firebase with credentials from environment variable


# Active player sessions


@app.route('/signin', methods=['POST'])
def signin():
    # THIS IS JUST AN EXAMPLE. WE SHOULD NOT HAVE VALIDATION HERE. IT SHOULD BE ANOTHER FUNCTION IN ANOTHER FILE.
    # We would just call it here. This example is just to show u guys how everything works.
    
    # Extract the username and password from the request
    data = request.json
    username = data.get('username')
    password = data.get('password')

    print("Hi Ryan")
    if username == "admin" and password == "password":
        return jsonify({"message": "Successfully signed in"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


from GameModule.gameCreationFunctions import createGameForPlayer


from UserModule.PlayerSessionManager import PlayerSessionManager
from UserModule.Player import Player


playerManager : PlayerSessionManager = PlayerSessionManager() # SINGLETON
userID : str = "bo3bw4GUJdFhTp6aEqiD"
tempPlayer : Player = Player(userID=userID)
tempPlayer.name = "Rayyan"
playerManager.addPlayer(userID,tempPlayer)


@app.route('/setGameForPlayer' , methods = ['GET'])

def getGameInfo():

    data = request.json

    gameDifficultyLevel : str = data['gameDifficultyLevel']
    userID : str = data['userID']


    # temp for testing
    userID : str = "bo3bw4GUJdFhTp6aEqiD"


    currentPlayer : Player = playerManager.getPlayer(playerID=userID)

    print(currentPlayer.userID)

    createGameForPlayer(currentPlayer,gameDifficultyLevel)

    print(f"Created {gameDifficultyLevel} game for {currentPlayer.name}")
    

    

    return jsonify({"message" : "Either successfully got a game, or no more games available to play for this difficulty"})


if __name__ == '__main__':
    app.run(port=5000)









# Below this are just example functions. They are not part of the application.



# Example Functions using firebase

EasyGames_ref = db.collection('EasyGames')
EasyRounds_ref = db.collection('EasyRounds')
images_ref = db.collection('images')
leaderboard_ref = db.collection('leaderboard')
players_ref = db.collection('players')


# Function to retrieve data from Firestore
def get_EasyGames_ref_data():
    docs = EasyGames_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict

def get_EasyRounds_ref_data():
    docs = EasyRounds_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict

def get_images_data():
    docs = images_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict


def get_leaderboard_data():
    docs = leaderboard_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict

def get_players_data():
    docs = players_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict

@app.route('/getEasyGames', methods=['GET'])
def getEasyGames():
    print(get_EasyGames_ref_data())

@app.route('/getEasyRounds', methods=['GET'])
def getEasyRounds():
    print(get_EasyRounds_ref_data())

@app.route('/getImages', methods=['GET'])
def getImages():
    print(get_images_data())

@app.route('/getLeaderboard', methods=['GET'])
def getLeaderboard():
    print(get_leaderboard_data())

@app.route('/getPlayers', methods=['GET'])
def getPlayers():
    print(get_players_data())

@app.route('/images', methods=['GET'])
def get_images():
    images_data = get_images_data()
    return jsonify(images_data)

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    leaderboard_data = get_leaderboard_data()
    return jsonify(leaderboard_data)

@app.route('/easyGames', methods=['GET'])
def get_easyGames():
    easyGames_data = getEasyGames()
    return jsonify(easyGames_data)

@app.route('/easyRounds', methods=['GET'])
def get_easyRounds():
    easyRounds_data = getEasyRounds()
    return jsonify(easyRounds_data)

@app.route('/players', methods=['GET'])
def get_players():
    players_data = get_players_data()
    return jsonify(players_data)










