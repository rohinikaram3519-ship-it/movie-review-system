import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    
    return " ".join(words)