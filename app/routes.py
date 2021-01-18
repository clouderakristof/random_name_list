from flask import Flask, render_template
import random
import os.path
app = Flask(__name__)

random_team_list = []

def file_writer(filename, list_to_write):
   with open(filename, 'w') as filehandle:
       filehandle.writelines("%s\n" % list_element for list_element in list_to_write)

def file_reader(filename):

    name_list = []

    # open file and read the content in a list
    with open(filename, 'r') as filehandle:
        filecontents = filehandle.readlines()

        for line in filecontents:
            # remove linebreak which is the last character of the string
            current_name = line[:-1]

            # add item to the list
            name_list.append(current_name)
        return name_list

@app.route('/')
def index():
    return "Please visit the /list page"

@app.route('/mix')
def mix():
    team_list = ["ckoncz", "zsfekete", "dkelencz", "kmolnosi", "odozsa", "gtoth"]
    global random_team_list
    file_writer('listfile.txt', random.sample(team_list,len(team_list)))
    return "Mixed!!! Please visit the /list page"


@app.route('/list')
def hello_world():
    if not os.path.isfile('listfile.txt'):
        mix()
    random_team_list=file_reader('listfile.txt')
    #return '\n'.join(random_team_list)
    return render_template('list.html', random_team_list=file_reader('listfile.txt'))
