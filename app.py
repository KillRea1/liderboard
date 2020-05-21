from flask import Flask, render_template

app = Flask(__name__)


class Player:
    def __init__(self, identifier, name, time):
        self.identifier = identifier
        self.name = name
        self.time = time


players = [
    Player(2, "Yellow", 1103),
    Player(1, "Black", 1023),
    Player(3, "White", 1023),
    Player(5, "Pink", 894),
    Player(4, "Green", 705),
    Player(6, "Blue", 602)
]


@app.route('/')
def hello_world():
    return render_template("leaderboard.html",
                           players=players,
                           len=len(players))


if __name__ == '__main__':
    app.run()
