
# **Sentiment Scraper API**

## **Project Description**
This project is a **Sentiment Scraper API** that scrapes **Reddit posts**, performs **sentiment analysis** using **TextBlob**, and sends the results via **email**. It leverages **Streamlit** for the **user interface** and includes automation for **scraping**, **analysis**, and **email reporting**.

The repository has gone through several stages of improvement, debugging, and optimization, making it suitable for real-world use cases and automating sentiment analysis.

---

## **Features**
- **Web Scraping**: Scrapes Reddit posts from the `r/Python` subreddit using **BeautifulSoup** and **requests**.
- **Sentiment Analysis**: Analyzes the sentiment of posts using **TextBlob** and classifies them as **Positive**, **Negative**, or **Neutral** based on the polarity score.
- **Email Reports**: Automatically sends a **sentiment analysis report** to a user-provided email address using **Gmail API**.
- **Streamlit UI**: Provides a user-friendly interface to interact with the app, input the recipient’s email, and view/download the sentiment analysis report.

---

## **Technologies Used**
- **Python** (version 3.12)
- **Streamlit**: For the user interface.
- **BeautifulSoup** and **requests**: For web scraping Reddit.
- **TextBlob**: For sentiment analysis.
- **Gmail API**: For sending emails with the sentiment report.

---

## **Installation Instructions**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/sentiment-scraper-api.git
   cd sentiment-scraper-api
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scriptsctivate     # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download `credentials.json`** for Gmail API from [Google Developer Console](https://console.cloud.google.com/).
   - Place it in the root directory of the project (same directory as `app.py`).

---

## **How to Run the Project**
1. **Run the Streamlit app**:
   ```bash
   streamlit run src/app.py
   ```

2. The app will open in your browser. Enter the recipient's email and click **"Start Scraping and Analyze Sentiment"**.

3. **The app will perform the following**:
   - Scrape Reddit posts from the `r/Python` subreddit.
   - Perform sentiment analysis on the posts.
   - Generate a **CSV report** with sentiment analysis results.
   - Send the report to the **email address** you provide.

---

## **Troubleshooting & Error Report**
### **Error**: **OSError: Cannot save file into a non-existent directory: 'data'**
- **Problem**: The app was unable to save the CSV file due to the **`data`** directory not existing.
- **Solution**: Ensured the **`data`** directory is created before saving the file. The directory is now automatically created using `os.makedirs()`.

### **Error**: **`NameError: name 'receiver_email' is not defined`**
- **Problem**: The **`receiver_email`** variable was not properly defined or passed in the **Streamlit UI**.
- **Solution**: The **`receiver_email`** input field in **Streamlit** was properly handled and passed into the **email-sending function**.

### **Error**: **`streamlit.errors.StreamlitDuplicateElementId`**
- **Problem**: Duplicate element IDs in **Streamlit input fields** caused an error.
- **Solution**: The `key` argument was added to the **Streamlit widgets** to ensure unique element IDs.

### **Error**: **`NameError: name 'receiver_email' is not defined` in Streamlit UI**
- **Problem**: The **`receiver_email`** variable was not properly defined inside the `Streamlit` function scope.
- **Solution**: Ensure that **`receiver_email`** is captured from **Streamlit's input** and passed correctly to the **`send_email()`** function.

---

## **License & Acknowledgments**
- **License**: MIT License (optional, if you want to include it)
- **Acknowledgments**: Thanks to **Google**, **TextBlob**, and **Streamlit** for the powerful APIs and libraries used in this project.

---

### **Steps to Push to GitHub**
1. **Verify no sensitive files** are committed in the repository:
   - **`token.pickle`** and **`credentials.json`** were removed from the history using **BFG Repo-Cleaner** or **`git filter-repo`**.
   - Added **`token.pickle`** and **`credentials.json`** to `.gitignore`.
