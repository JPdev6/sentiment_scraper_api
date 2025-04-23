
# **Sentiment Scraper API 🚀**

## **Project Description 📚**
Welcome to the **Sentiment Scraper API**! This project allows you to scrape **Reddit posts**, perform **sentiment analysis** using **TextBlob**, and send the results via **email** using the **Gmail API**. The application is powered by **Streamlit** for creating a user-friendly interface that allows users to trigger the scraping, sentiment analysis, and email report generation.

This project is perfect for automating sentiment analysis tasks, especially if you are interested in analyzing **Reddit posts** or **comments** on specific topics!

---

## **Features 🎯**
- **Web Scraping**: 
  - Scrapes Reddit posts from the `r/Python` subreddit using **BeautifulSoup** and **requests**.
- **Sentiment Analysis**: 
  - Analyzes the sentiment of posts using **TextBlob**.
  - Classifies posts into **Positive**, **Negative**, or **Neutral** based on the **polarity** score.
- **Email Reports**: 
  - Automatically sends a **sentiment analysis report** to a user-provided email address using the **Gmail API**.
- **Streamlit UI**: 
  - Provides a clean and simple interface where users can input the recipient’s email, start scraping, and view/download the sentiment analysis results.

---

## **Technologies Used ⚙️**
- **Python** (version 3.12)
- **Streamlit**: Interactive web application framework for easy UI.
- **BeautifulSoup** and **requests**: For scraping Reddit.
- **TextBlob**: For sentiment analysis (polarity and subjectivity).
- **Gmail API**: For sending emails with the sentiment report.
- **Git**: Version control for the project repository.

---

## **Installation Instructions 🛠️**

### **Clone the repository**:
```bash
git clone https://github.com/yourusername/sentiment-scraper-api.git
cd sentiment-scraper-api
```

### **Set up a virtual environment**:
(It's highly recommended to use a virtual environment to isolate dependencies)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scriptsctivate     # On Windows
```

### **Install dependencies**:
Make sure all the dependencies are installed with:
```bash
pip install -r requirements.txt
```

### **Download credentials**:
- **Gmail API credentials** are required to send emails. You can download the **`credentials.json`** from the [Google Developer Console](https://console.cloud.google.com/).
- Place the `credentials.json` file in the **root directory** of the project (same folder as `app.py`).

---

## **How to Run the Project 🚀**
1. **Run the Streamlit app**:
```bash
streamlit run src/app.py
```

2. **Streamlit Interface** will open in your browser. Here’s how the app works:
   - **Input recipient email**: Enter the email address where you want the sentiment analysis report to be sent.
   - **Start Scraping & Analyzing Sentiment**: Click the button to scrape Reddit posts from the `r/Python` subreddit and perform sentiment analysis.
   - **Download Report**: After the sentiment analysis, download the **CSV report** containing the sentiment results.

---

## **Troubleshooting & Error Report 🐞**
### **Error 1**: **OSError: Cannot save file into a non-existent directory: 'data'**
- **Problem**: The app couldn’t save the CSV file because the **`data`** directory was not created.
- **Solution**: Ensured the **`data`** directory is created automatically using `os.makedirs()` before attempting to save the file.

### **Error 2**: **`NameError: name 'receiver_email' is not defined`**
- **Problem**: The **`receiver_email`** variable wasn’t correctly passed to the email-sending function.
- **Solution**: Properly handled the **`receiver_email`** in **Streamlit** and passed it into the email-sending function.

### **Error 3**: **`streamlit.errors.StreamlitDuplicateElementId`**
- **Problem**: Duplicate **element IDs** in **Streamlit input fields** caused an error.
- **Solution**: Added a **`key`** argument to **Streamlit widgets** to ensure unique IDs for each element.

### **Error 4**: **`NameError: name 'receiver_email' is not defined` in Streamlit UI**
- **Problem**: The **`receiver_email`** variable wasn’t properly captured or passed in the **Streamlit UI**.
- **Solution**: Captured the **`receiver_email`** input correctly in Streamlit and passed it to the **`send_email()`** function.

---

## **How to Contribute 🤝**

We welcome contributions! Feel free to fork the repository, submit issues, or create pull requests to improve the project. Here’s how you can contribute:
1. Fork the repository.
2. Clone your fork to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them.
5. Push your changes and open a pull request.

---

## **License & Acknowledgments 📝**
- **License**: MIT License (optional, if you want to include it).
- **Acknowledgments**: Special thanks to **Google**, **TextBlob**, and **Streamlit** for providing the powerful APIs and libraries used in this project.

---

## **Steps to Push to GitHub 📤**
1. **Verify no sensitive files** are committed in the repository:
   - **`token.pickle`** and **`credentials.json`** were removed from the history using **BFG Repo-Cleaner** or **`git filter-repo`**.
   - Added **`token.pickle`** and **`credentials.json`** to `.gitignore`.

---

### **Badges & Links 📛**
- [![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org)
- [![Streamlit](https://img.shields.io/badge/Streamlit-1.0-green.svg)](https://streamlit.io)
- [![GitHub License](https://img.shields.io/github/license/JPdev6/sentiment_scraper_api)](https://github.com/JPdev6/sentiment_scraper_api/blob/master/LICENSE)
