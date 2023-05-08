
# https://www.pythonanywhere.com/user/imvickykumar999/tasks_tab/
import requests

def send_link(bot_message = f'''
Good morning, 
Here is today's news.

https://imvickykumar999.pythonanywhere.com/
'''):
  
  bot_token = '**********:*****************************'
  # https://t.me/BotFather

  gets = f'https://api.telegram.org/bot{bot_token}/getUpdates'
  req = requests.get(gets) 

  show = req.json()
  lst = list(show.values())[1]
  unique = []

  for i in lst:
    bot_chatID = i['message']['chat']['id']
    name = i['message']['chat']['first_name']
    unique.append(bot_chatID)

  for i in set(unique):
    sets = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={i}&parse_mode=Markdown&text={bot_message}'    
    requests.post(sets)

def send_news():
  bot_token = '**************************'
  # https://newsapi.org/account

  gets = f'https://newsapi.org/v1/articles?source=the-verge&sortBy=top&apiKey={bot_token}'
  req = requests.get(gets) 
  box = req.json()['articles']

  for i in box:
    bot_message = f'''
{i['title']}

{i['description']}

{i['url']}
'''
    send_link(bot_message)

send_link()
send_news()
