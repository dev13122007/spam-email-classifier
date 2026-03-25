# Spam Email Checker 📧

This is a simple machine learning project that checks whether an email is spam or not spam. The idea behind this project was to understand how text classification works and how a trained model can be used in a small real-world example.

Instead of making it too complex, I kept the project simple and focused on the core idea — taking email text, processing it, and predicting the result.

---

## What this project does

* Takes email text as input
* Cleans the text using basic preprocessing
* Converts text into numerical form using TF-IDF
* Uses a trained model to classify the email
* Displays whether the email is spam or not spam

---

## Project Structure

```
Spam_Email_Classifier/
│
├── data/
│   └── spam.csv
│
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── preprocess.py
├── train.py
├── email_checker.py
└── requirements.txt
```

---

## How to Run

Go to the project folder

```
cd Spam_Email_Classifier
```

Install dependencies

```
pip install -r requirements.txt
```

Train the model

```
python train.py
```

Run the email checker

```
python email_checker.py
```

---

## How to Use

* Enter the email text in terminal
* Press enter
* The model will predict spam or not spam
* Choose whether to check another email

---

## Sample Inputs

Spam example

```
Congratulations! You have won a free prize
```

Not spam example

```
Hi, are we meeting tomorrow for the project
```

---

## What I Learned

* Basic text preprocessing
* TF-IDF vectorization
* Naive Bayes classification
* Saving and loading trained models
* Building a simple terminal based tool

---

## Notes

This is a basic learning project.
The accuracy depends on the dataset used for training.
The model can be improved further by adding more data.

---

## Author

Divyansh Gupta

---

This project was created as part of learning machine learning fundamentals and understanding how classification models work with text data.
