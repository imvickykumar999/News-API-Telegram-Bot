
import requests, random
from flask import Flask, render_template, send_from_directory
import predict_news as pn

app = Flask(__name__)

@app.route('/<filename>')
def ads(filename):
    if '.' in filename:
        filename = 'ads.txt'
    return send_from_directory("", filename)

def get_news(source):
    try:
        bot_token = '87623b8db3254e8698e239abc51a9c10'
        gets = f'https://newsapi.org/v1/articles?source={source}&sortBy=top&apiKey={bot_token}'
        
        req = requests.get(gets) 
        box = req.json()['articles']

    except:
        try:
            bot_token = 'e1b57251b1b94ed894f3c60d25551eb2'
            gets = f'https://newsapi.org/v1/articles?source={source}&sortBy=top&apiKey={bot_token}'
            
            req = requests.get(gets) 
            box = req.json()['articles']

        except:
            bot_token = '5f69434d32434ea8bdb16b347f71cca2'
            gets = f'https://newsapi.org/v1/articles?source={source}&sortBy=top&apiKey={bot_token}'
            
            req = requests.get(gets) 
            box = req.json()['articles']

    ha,ia,ba,la,pa = [],[],[],[],[]
    for i in range(len(box)):
        h = box[i]['title']
        m = box[i]['urlToImage']
        b = box[i]['description']
        p = pn.predict_category(b)

        try:
            l = box[i]['url']
        except:
            l = 'link not found'

        ha.append(h)
        ia.append(m)
        ba.append(b)
        la.append(l)
        pa.append(p)
    return ha, ia, ba, la, pa

@app.route('/news/<source>')
def one_news(source):
    
    ha, ia, ba, la, pa = get_news(source)
    return render_template('news.html', 
                            ha=ha, 
                            ia=ia, 
                            ba=ba, 
                            la=la, 
                            pa=pa,
                            len = len(ha))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
def news():
    source = ['bbc-news', 'cnn', 'the-verge', 'time', 'the-wall-street-journal']
    source = random.choice(source)

    ha, ia, ba, la, pa = get_news(source)
    return render_template('news.html', 
                            ha=ha, 
                            ia=ia, 
                            ba=ba, 
                            la=la,
                            pa=pa, 
                            len = len(ha))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(
        # host="0.0.0.0", 
        debug=False
    )
