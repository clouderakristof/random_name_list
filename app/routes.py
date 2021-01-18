from flask import Flask, render_template
import random
app = Flask(__name__)

random_team_list = []

@app.route('/')
def index():
    team_list = ["ckoncz", "zsfekete", "dkelencz", "kmolnosi", "odozsa", "gtoth"]
    global random_team_list
    random_team_list = random.sample(team_list,len(team_list))
    return "Please visit the /list page"

@app.route('/mix')
def mix():
    team_list = ["ckoncz", "zsfekete", "dkelencz", "kmolnosi", "odozsa", "gtoth"]
    global random_team_list
    random_team_list = random.sample(team_list,len(team_list))
    return "Mixed! Please visit the /list page"

@app.route('/list')
def hello_world():
    global random_team_list
    #return '\n'.join(random_team_list)
    return render_template('list.html', random_team_list=random_team_list)
