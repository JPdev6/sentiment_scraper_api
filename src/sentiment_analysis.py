import pandas as pd
from textblob import TextBlob
from typing import List, Dict



# # Example posts (from Reddit scrape)
# posts = [
#     "I love Python! It's such a powerful language.",
#     "I hate when the code doesn't work. It’s so frustrating.",
#     "This is a neutral post, not much emotion here."
# ]
def analyze_sentiment(titles: List[str]) -> List[Dict]:    # Get post-titles by scraping
    results = []
    # Analyzing the sentiment of each post
    for post in titles:
        blob = TextBlob(post)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        results.append({"Post": post, "Sentiment": sentiment, "Polarity": polarity})

    return results

