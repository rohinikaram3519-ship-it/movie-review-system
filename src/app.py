import streamlit as st
from sentiment import get_sentiment
from aspect import extract_aspects
from emotion import detect_emotion
from summarizer import summarize

st.set_page_config(page_title="Movie AI", layout="centered")

st.title("Movie Review Analyzer")

review = st.text_area("Enter Movie Review")

if st.button("Analyze"):
    if review:
        sentiment, score = get_sentiment(review)
        aspects = extract_aspects(review)
        emotion = detect_emotion(review)
        summary = summarize(review)

        st.subheader("Sentiment")
        st.write(sentiment, score)

        st.subheader("Aspects")
        st.write(aspects)

        st.subheader("Emotions")
        for emotion, score in emotion.items():
            st.progress(score / 100)
            st.write(f"{emotion.capitalize()} : {score}%")
        

        st.subheader("Summary")
        st.write(summary)