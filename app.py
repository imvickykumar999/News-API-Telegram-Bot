
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/news')
def news():

    bot_token = '*********************'
    # https://newsapi.org/account
    
    gets = f'https://newsapi.org/v1/articles?source=the-verge&sortBy=top&apiKey={bot_token}'
    req = requests.get(gets) 
    box = req.json()['articles']

    ha,ia,ba,la = [],[],[],[]
    for i in range(len(box)):
        h = box[i]['title']
        m = box[i]['urlToImage']
        b = box[i]['description']
        l='link not found'

        try:
            l = box[i]['url']
        except:
            pass

        ha.append(h)
        ia.append(m)
        ba.append(b)
        la.append(l)
    return render_template('news.html', ha=ha, ia=ia, ba=ba, la=la, len = len(ha))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
