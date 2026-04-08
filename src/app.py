import streamlit as st
import matplotlib.pyplot as plt

from sentiment import get_sentiment
from aspect import extract_aspects
from emotion import detect_emotion
from summarizer import summarize

st.set_page_config(page_title="Movie Sentiment Analysis", layout="centered")

st.title("Movie Review Analyzer")

review = st.text_area("Enter Movie Review")

if st.button("Analyze"):
    if review:

        sentiment, score = get_sentiment(review)
        aspects = extract_aspects(review)
        emotion = detect_emotion(review)

        if isinstance(emotion, list):
            emotion = {emotion[0]['label']: int(emotion[0]['score'] * 100)}

        summary = summarize(review)

        st.subheader("Sentiment")
        st.write(f"{sentiment} ({round(score,2)})")

        st.subheader("Aspects")
        st.write(aspects)

        st.subheader("Emotions")

        for emo, val in emotion.items():  
            st.progress(val / 100)
            st.write(f"{emo.capitalize()} : {val}%")

        st.subheader("Emotion Bar Chart")

        emotions_names = list(emotion.keys())
        scores = list(emotion.values())

        plt.figure()
        plt.bar(emotions_names, scores)
        plt.xlabel("Emotions")
        plt.ylabel("Score (%)")

        st.pyplot(plt)
        st.subheader("Emotion Pie Chart")
        filtered_emotions = {k: v for k, v in emotion.items() if v > 3}

        labels = list(filtered_emotions.keys())
        scores = list(filtered_emotions.values())  

        if len(labels) == 0:
           st.write("No significant emotions to display")
        else:
           plt.figure()
           plt.pie(scores, labels=labels, autopct='%1.1f%%')
           st.pyplot(plt)
        
        st.subheader("Summary")
        st.write(summary)
