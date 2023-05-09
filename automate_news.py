
# https://www.pythonanywhere.com/user/imvickykumar999/tasks_tab/
import requests, random

def send_link(bot_message):
  bot_token = '************************'
  # https://t.me/BotFather

  gets = f'https://api.telegram.org/bot{bot_token}/getUpdates'
  req = requests.get(gets) 

  show = req.json()
  lst = list(show.values())[1]
  unique = []

  for i in lst:
    bot_chatID = i['message']['chat']['id']
    unique.append(bot_chatID)

  for i in set(unique):
    sets = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={i}&parse_mode=Markdown&text={bot_message}'    
    requests.post(sets)

def send_news():
  bot_token = '*********************'
  # https://newsapi.org/account

  source = ['the-hindu', 'the-times-of-india', 'bbc-news', 'cnn', 
            'the-verge', 'time', 'the-wall-street-journal', ]
  
  source = random.choice(source)
  print(source)
  
  bot_message = f'''
Good morning ☀️
Here is today's news from {source.upper()}

https://imvickykumar999.pythonanywhere.com/

Reply me with any sticker to continue daily.
'''

  send_link(bot_message)
  gets = f'https://newsapi.org/v1/articles?source={source}&sortBy=top&apiKey={bot_token}'
  
  req = requests.get(gets) 
  box = req.json()['articles']

  for i in box:
    if i['description'] == None:
      i['description'] = 'Read More'

    bot_message = f'''
➡️ {i['title']}

{i['description']}

{i['url']}
'''
    send_link(bot_message)

try:
  print('1st')
  send_news()
except:
  try:
    print('2nd')
    send_news()
  except:
    try:
      print('3rd')
      send_news()
    except:
      print('4th')
      send_news()
