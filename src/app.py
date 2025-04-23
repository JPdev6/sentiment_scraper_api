import os

import pandas as pd
import streamlit as st

from email_sender import send_email, authenticate_google_account
from scraper import get_post_titles
from sentiment_analysis import analyze_sentiment


def automate_process():
    # Scrape Reddit posts
    post_titles = get_post_titles()

    # Perform sentiment analysis
    sentiment_results_list = analyze_sentiment(post_titles)

    # Ensure the directory exists
    save_directory = 'data'
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)  # Create the directory if it doesn't exist

    # Save results to CSV
    file_path1 = os.path.join(save_directory, 'sentiment_report.csv')
    df = pd.DataFrame(sentiment_results_list)
    df.to_csv(file_path1, index=False)

    # Authenticate with Google and get the service
    service = authenticate_google_account()

    if service:
        sender_email = 'johnnycontactmail@gmail.com'
        recipient_email = st.text_input("Recipient Email", 'jenny93meta@gmail.com')
        subject = 'Sentiment Analysis Report'
        body = "Please find the attached sentiment analysis report."

        # Send the email with the sentiment report attached
        send_email(service, sender_email, recipient_email, subject, body, attachment_path=file_path1)

    return file_path1, sentiment_results_list


# Streamlit UI
st.title("Sentiment Scraper and Analysis")

st.write(
    "This app scrapes Reddit posts, performs sentiment analysis, and sends the results via email."
)

# Input field for the recipient email
receiver_email = st.text_input("Recipient Email", "jenny93meta@gmail.com",key="receiver_email_input")

# Button to start scraping and analyzing sentiment
if st.button("Start Scraping and Analyze Sentiment"):
    if receiver_email:
        with st.spinner("Processing..."):
            file_path, sentiment_results = automate_process()
            st.success("Process completed successfully!")

            # Show sentiment analysis results
            st.write("Sentiment Analysis Report:")
            st.dataframe(pd.DataFrame(sentiment_results))  # Display the DataFrame with the results

            # Provide download button for the sentiment report
            if os.path.exists(file_path):  # Ensure the file exists before trying to download
                with open(file_path, "rb") as file:
                    st.download_button(
                        label="Download Sentiment Report",
                        data=file.read(),
                        file_name="sentiment_report.csv",
                        mime="text/csv",
                    )

            # Notify the user about email sending
            st.write(f"Sentiment report has been sent to {receiver_email}.")
    else:
        st.error("Please enter a valid email address.")
else:
    st.write("Click the button to start the process.")
