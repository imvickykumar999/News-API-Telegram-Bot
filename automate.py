
# https://www.pythonanywhere.com/user/imvickykumar999/tasks_tab/
import requests

bot_token = input('Enter Bot Token : ')
# bot_token = '************************'
# https://newsapi.org/account

gets = f'https://api.telegram.org/bot{bot_token}/getUpdates'
req = requests.get(gets) 

show = req.json()
lst = list(show.values())[1]

unique = []

for i in lst:
  bot_chatID = i['message']['chat']['id']
  name = i['message']['chat']['first_name']
  unique.append((bot_chatID, name))

print(set(unique))

for i in set(unique):
  bot_message = f'''
Good morning {i[1]}, 
Here is today's news.

https://imvickykumar999.pythonanywhere.com/news
'''

  sets = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={i[0]}&parse_mode=Markdown&text={bot_message}'    
  requests.post(sets)
