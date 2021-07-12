from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return index()


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/movie')
def movie():
    datalist = []
    conn = sqlite3.connect("movie250.db")
    cur = conn.cursor()
    sql = '''
        SELECT * FROM movie250
    '''
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template("movie.html", movies=datalist)


@app.route('/rates')
def rates():
    score = []  # rate
    cnt = []  # number of movies in one score
    conn = sqlite3.connect("movie250.db")
    cur = conn.cursor()
    sql = '''
            SELECT rate, count(rate) FROM movie250 GROUP BY rate;
        '''
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        cnt.append(item[1])
    cur.close()
    conn.close()
    return render_template("rates.html", score=score, cnt=cnt)


@app.route('/words')
def words():
    return render_template("words.html")


@app.route('/team')
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run()
