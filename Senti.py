import streamlit as st
import nltk

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Function for sentiment analysis
def analyze_sentiment(text):
    from nltk.sentiment import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    sentiment_score = sentiment_scores['compound']

    if sentiment_score >= 0.05:
        sentiment_label = 'Positive'
        emoji = '😊'  # Green emoji
        color = 'green'
    elif sentiment_score <= -0.05:
        sentiment_label = 'Negative'
        emoji = '😞'  # Red emoji
        color = 'red'
    else:
        sentiment_label = 'Neutral'
        emoji = '😐'  # Yellow emoji
        color = 'yellow'

    return sentiment_label, sentiment_score, emoji, color

# Streamlit app
def main():
    st.title('Sentiment Analysis App')

    # Text input for user to enter text with a placeholder example
    example_tweet = "I do not like this campaign"
    user_text = st.text_area('Enter text for sentiment analysis:', value=example_tweet)

    if st.button('Analyze Sentiment'):
        if user_text:
            sentiment_label, sentiment_score, emoji, color = analyze_sentiment(user_text)

            # Display sentiment label with emoji and color
            st.write(f'Sentiment Label: <span style="color:{color}">{sentiment_label} {emoji}</span>', unsafe_allow_html=True)
            
            # Display sentiment score
            st.write(f'Sentiment Score: {sentiment_score}')

if __name__ == '__main__':
    main()
