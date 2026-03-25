import pickle
from preprocess import clean_text

print("=" * 35)
print("       Spam Email Checker")
print("=" * 35)

with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

while True:

    print("\nEnter Email Text:")
    email = input("> ")

    text = clean_text(email)
    vector = vectorizer.transform([text])

    pred = model.predict(vector)[0]

    if pred == "ham":
        result = "Not Spam"
    else:
        result = "Spam"

    print("\nResult :", result)

    print("\nCheck another email? (y/n)")
    choice = input("> ")

    if choice.lower() != "y":
        print("\nThank you for using Spam Email Checker.")
        break