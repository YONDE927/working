import json
from flask import Flask , render_template

application = Flask(__name__)

DATA_FILE='norilog.json'

def save_data(start,finish,memo,created_at):
    try:
        database=json.load(open(DATA_FILE,mode="r",encoding="utf-8"))
    except FileNotFoundError:
        database=[]

    database.insert(0,{"start":start,"finish":finish,"memo":memo,"created_at":created_at.strftime("%Y-%m-%d %H:%M")})

    json.dump(database, open(DATA_FILE,mode="w",encoding="utf-8"),indent=4,ensure_ascii=False)

def load_data():
    try:
        database=json.load(open(DATA_FILE,mode="r",encoding="utf-8"))
    except FileNotFoundError :
        database=[]
    return database

@application.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    application.run('0.0.0.0', 8000, debug=True)
