import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    words = text.split()
    new_words = []

    for w in words:
        if w not in stop_words:
            new_words.append(w)

    text = " ".join(new_words)

    return text