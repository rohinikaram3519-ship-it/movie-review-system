from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = sia.polarity_scores(text)['compound']

    if score > 0:
        return "Positive",score
    elif score < 0:
        return "Negative",score
    else:
        return "Neutral",score