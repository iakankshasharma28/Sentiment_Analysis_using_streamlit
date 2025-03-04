import os
import subprocess

# Ensure required libraries are installed
required_packages = ["nltk", "textblob", "matplotlib", "wordcloud", "streamlit"]
for package in required_packages:
    subprocess.run(["pip", "install", package])

# Now import after installation
import streamlit as st
import nltk
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# Download necessary NLTK resources
nltk.download('punkt')

# Set Page Configuration (Must be First)
st.set_page_config(page_title="Sentiment Analyzer", layout="centered", page_icon="🔍")

# Custom CSS for Navbar and Styling
st.markdown("""
    <style>
        /* Navbar Styling */
        .navbar {
            background-color: #2E86C1;
            padding: 15px;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            color: white;
            border-radius: 10px;
        }

        /* Subtitle */
        .subtitle {
            text-align: center;
            font-size: 20px;
            color:rgb(13, 127, 240);
        }

        /* Developed by */
        .developed-by {
            text-align: center;
            font-size: 16px;
            color: gray;
            margin-top: -10px;
        }

        /* Buttons */
        .stButton>button {
            background-color: #2E86C1;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            transition: all 0.3s ease-in-out;
        }

        .stButton>button:hover {
            background-color: #1B4F72;
        }

        /* Footer */
        .footer {
            text-align: center;
            margin-top: 50px;
            color: gray;
        }
    </style>
""", unsafe_allow_html=True)

# Navbar Title
st.markdown('<div class="navbar">🔍 Sentiment Analyzer</div>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Analyze the sentiment of your text instantly.</p>', unsafe_allow_html=True)
st.markdown('<p class="developed-by">Developed by Akanksha Sharma</p>', unsafe_allow_html=True)

# Start Application Button
start_clicked = st.button("Start Application")
if start_clicked:
    st.success("Application Started! Enter a sentence below.")

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    return sentiment_score

# Function to extract positive & negative words
def split_sentiment(text):
    words = text.split()
    positive_words = []
    negative_words = []

    for word in words:
        sentiment = TextBlob(word).sentiment.polarity
        if sentiment > 0:
            positive_words.append(word)
        elif sentiment < 0:
            negative_words.append(word)
    
    return " ".join(positive_words), " ".join(negative_words)

# User Input Section
st.write("### Enter Your Sentence:")
user_input = st.text_area("Type your text here...", height=100)

# Analyze Button
if st.button("Analyze Sentiment"):
    if user_input:
        sentiment_score = analyze_sentiment(user_input)
        positive_part, negative_part = split_sentiment(user_input)

        # Display Sentiment Results
        if sentiment_score > 0:
            st.success("Overall Sentiment: **Positive** 😊")
        elif sentiment_score < 0:
            st.error("Overall Sentiment: **Negative** 😞")
        else:
            st.warning("Overall Sentiment: **Neutral** 😐")

        # Display Positive & Negative Words
        st.write(f"**Positive Words:** {positive_part}")
        st.write(f"**Negative Words:** {negative_part}")

        # Word Cloud Visualization
        wordcloud = WordCloud(width=400, height=200, background_color='white').generate(user_input)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)

    else:
        st.warning("⚠ Please enter a sentence before analyzing.")

# Feedback Section
st.subheader("📩 Leave Your Feedback")
feedback_file = "feedback.csv"

def save_feedback(name, contact, message):
    feedback_data = pd.DataFrame([[name, contact, message]], columns=["Name", "Contact", "Message"])
    if os.path.exists(feedback_file):
        feedback_data.to_csv(feedback_file, mode='a', header=False, index=False)
    else:
        feedback_data.to_csv(feedback_file, mode='w', header=True, index=False)

with st.form("feedback_form"):
    name = st.text_input("Your Name")
    contact = st.text_input("Your Contact (Email/Phone)")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Submit Feedback")
    if submitted:
        save_feedback(name, contact, message)
        st.success("Thank you for your feedback! 😊")

# Exit Application with Thank You GIF
def exit_application():
    st.image("https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif", width=400)
    st.markdown("## Thank You for Using Sentiment Analyzer! 😊")
    st.write("We appreciate your feedback. Let us know your thoughts below!")

    st.success("Closing Application...")

    # Close Streamlit & CMD Window
    os._exit(0)

# Exit Button
exit_clicked = st.button("Exit Application")
if exit_clicked:
    exit_application()

# Footer Section with Social Icons
st.markdown("""
    <hr>
    <div class="footer">
        <p>© 2025 Akanksha Sharma | Connect with me:</p>
        <p>
            <a href="https://linkedin.com/in/iakankshasharma28" target="_blank">
                <img src="https://img.icons8.com/fluency/48/000000/linkedin.png" width="32">
            </a>
            &nbsp;&nbsp;
            <a href="mailto:iakankshasharma28@gmail.com">
                <img src="https://img.icons8.com/fluency/48/000000/gmail.png" width="32">
            </a>
            &nbsp;&nbsp;
            <a href="https://github.com/iakankshasharma28" target="_blank">
                <img src="https://img.icons8.com/fluency/48/000000/github.png" width="32">
            </a>
            &nbsp;&nbsp;
            <a href="https://instagram.com/iakankshasharma__" target="_blank">
                <img src="https://img.icons8.com/fluency/48/000000/instagram-new.png" width="32">
            </a>
        </p>
    </div>
""", unsafe_allow_html=True)
