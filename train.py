import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from preprocess import clean_text

data = pd.read_csv('data/spam.csv')

data['text'] = data['text'].apply(clean_text)

text = data['text']
label = data['label']

vectorizer = TfidfVectorizer()
text_vector = vectorizer.fit_transform(text)

model = MultinomialNB()
model.fit(text_vector, label)

with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('models/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Model trained successfully!")