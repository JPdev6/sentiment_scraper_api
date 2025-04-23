# Sentiment Scraper API

## Project Description
This project is a **Sentiment Scraper API** that scrapes Reddit posts, performs sentiment analysis on the posts using **TextBlob**, and sends the results via **email**. It is built using **Streamlit** for the user interface and includes automation for regular scraping, analysis, and email reporting.

## Features
- **Web Scraping**: Scrapes Reddit posts from the `r/Python` subreddit using **BeautifulSoup** and **requests**.
- **Sentiment Analysis**: Analyzes the sentiment of posts using **TextBlob** and classifies them as **Positive**, **Negative**, or **Neutral** based on polarity.
- **Email Reports**: Automatically sends a **sentiment analysis report** to a user-provided email address using **Gmail API**.
- **Streamlit UI**: Provides a user-friendly interface to interact with the project, input the recipient’s email, and view/download the sentiment analysis report.

## Technologies Used
- **Python** (version 3.12)
- **Streamlit**: For the user interface.
- **BeautifulSoup** and **requests**: For web scraping Reddit.
- **TextBlob**: For sentiment analysis.
- **Gmail API**: For sending emails with the sentiment report.

## Installation Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/JPdev6/sentiment-scraper-api.git
   cd sentiment-scraper-api
