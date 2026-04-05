from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

aspects = {
    "Acting": ["acting", "performance", "actor"],
    "Story": ["story", "plot", "script"],
    "Music": ["music", "songs", "bgm"],
    "Direction": ["direction", "director"],
    "Visuals": ["visuals", "cinematography", "vfx"]
}

def extract_aspects(review):
    result = {}
    review_lower = review.lower()

    for aspect, keywords in aspects.items():
        for word in keywords:
            if word in review_lower:
                score = sia.polarity_scores(review)['compound']
                
                if score > 0:
                    result[aspect] = "Positive "
                elif score < 0:
                    result[aspect] = "Negative "
                else:
                    result[aspect] = "Neutral"
                break  
    
    return result