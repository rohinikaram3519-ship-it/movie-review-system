from transformers import pipeline

emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)

def detect_emotion(text):
    results = emotion_model(text)[0]
    
    emotions = {}
    for item in results:
        emotions[item['label']] = int(item['score'] * 100)
    
    return emotions