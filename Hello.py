import streamlit as st          #pip install streamlit
import nltk                     #pip install nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
s = SentimentIntensityAnalyzer()
st.set_page_config(page_title="Sentiment Analyser (BongTech Insights)")
st.title("Sentiment Analyser (BongTech Insights)")
text = st.text_area("Enter your text:")
if st.button("Analyze"):
    if text:
        sentiment_scores = s.polarity_scores(text)

        if sentiment_scores['compound'] >= 0.05:
            sentiment = 'Positive'
        elif sentiment_scores['compound'] <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        st.write("Text: ", text)
        st.write("Sentiment Scores: ", sentiment_scores)
        st.write("Sentiment: ", sentiment)
    else:
        st.warning("Please enter some text for analysis.")
