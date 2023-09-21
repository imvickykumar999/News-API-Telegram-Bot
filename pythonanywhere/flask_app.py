
r''' 
C:\Users\Vicky\Desktop\Repository\Host-Onion\Tor Browser\Browser\TorBrowser\Data\Tor\torrc

Open Tor Browser to host on Dark Web.
https://github.com/imvickykumar999/XAMPP-Onion-Host#for-flask-deployment

HiddenServiceDir C:/Users/Vicky/Desktop/Repository/Host-Onion/Tor Browser/HiddenService/sample_flask
HiddenServicePort 80 127.0.0.1:9151
'''

import requests, random
from flask import Flask, render_template
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

def get_news(source):
    if source == 'inshorts':

        link = 'https://inshorts.com/en/read'
        req = requests.get(link)

        soup = bs(req.content, 'html5lib')
        box = soup.findAll('div', attrs = {'class':'news-card z-depth-1'})

        ha,ia,ba,la = [],[],[],[]
        for i in range(len(box)):
            h = box[i].find('span', attrs = {'itemprop':'headline'}).text

            m = box[i].find('div', attrs = {'class':'news-card-image'})
            m = m['style'].split("'")[1]

            b = box[i].find('div', attrs = {'itemprop':'articleBody'}).text
            l = 'link not found'

            try:
                l = box[i].find('a', attrs = {'class':'source'})['href']
            except:
                pass
            
            ha.append(h)
            ia.append(m)
            ba.append(b)
            la.append(l)

    else:
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

        ha,ia,ba,la = [],[],[],[]
        for i in range(len(box)):
            h = box[i]['title']
            m = box[i]['urlToImage']
            b = box[i]['description']
            l = 'link not found'

            try:
                l = box[i]['url']
            except:
                pass

            ha.append(h)
            ia.append(m)
            ba.append(b)
            la.append(l)
    return ha, ia, ba, la

@app.route('/news/<source>')
def one_news(source):
    
    ha, ia, ba, la = get_news(source)
    return render_template('news.html', 
                            ha=ha, 
                            ia=ia, 
                            ba=ba, 
                            la=la, 
                            len = len(ha))

@app.route('/')
def news():
    source = ['the-hindu', 'the-times-of-india', 'bbc-news', 'cnn', 
              'the-verge', 'time', 'the-wall-street-journal', ]
    
    # https://newsapi.org/account
    source = random.choice(source)
    print(source)

    ha, ia, ba, la = get_news(source)
    # ha, ia, ba, la = get_news('inshorts')

    return render_template('news.html', 
                            ha=ha, 
                            ia=ia, 
                            ba=ba, 
                            la=la, 
                            len = len(ha))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':

    ## To uncomment, Open Tor Browser
    # from stem.control import Controller

    # port = 5000
    # host = "127.0.0.1"
    # hidden_svc_dir = "C:/Users/Vicky/Desktop/Repository/Host-Onion/Tor Browser/sample_flask"

    # print (" * Getting controller")
    # controller = Controller.from_port(address=host, port=9151)

    # try:
    #     controller.authenticate(password="")
    #     controller.set_options([
    #         ("HiddenServiceDir", hidden_svc_dir),
    #         ("HiddenServicePort", "80 %s:%s" % (host, str(port)))
    #         ])
    #     svc_name = open(hidden_svc_dir + "/hostname", "r").read().strip()
    #     print (" * Created host: %s" % svc_name)

    # except Exception as e:
    #     print (e)

    app.run(
        host="0.0.0.0", 
        debug=True
    )
