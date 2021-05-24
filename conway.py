#!/usr/bin/env/python3

from flask import Flask, render_template
from game import Game

app = Flask(__name__)

def play():
    global board
    g = Game(30, 100)
    board = g.next_gen()
    return board

@app.route("/", methods=["GET"])
def index():
    return render_template("board.html", tbl=play())






