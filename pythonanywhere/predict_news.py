
import pickle
from sklearn.datasets import fetch_20newsgroups

data=fetch_20newsgroups()
categories=data.target_names
train=fetch_20newsgroups(subset='train',categories=categories)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_category(s,train=train,model=model):
    pred=model.predict([s])
    return train.target_names[pred[0]]

# while True:
#     askme = input('\nEnter news headline : ')
#     predicted_news = predict_category(askme) 
#     print(predicted_news)
