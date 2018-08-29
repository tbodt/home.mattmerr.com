from flask import Flask, Response, render_template, request
from subprocess import Popen, PIPE
import random

app = Flask(__name__)

def RandomImage():
    images = tuple(open('images.txt', 'r'))
    return random.choice(images)

def Headline():
    p1 = Popen(["date", "-I"], stdout=PIPE)
    p2 = Popen(["toilet", "-f", "shadow"], stdin=p1.stdout, stdout=PIPE)
    p1.stdout.close()
    return p2.communicate()[0].decode("utf-8")

@app.route('/')
def Index():
    return render_template('index.html', image=RandomImage(), headline=Headline())

