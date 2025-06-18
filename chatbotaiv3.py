#!/usr/bin/env python3

import os
import streamlit as st
from PIL import Image # Keep this import if you plan to use image assets from 'assets' folder
import google.generativeai as genai

# --- Configuration for Local Environment ---
# Get API Key from environment variable
# IMPORTANT: Before running, set this in your terminal:
# export GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"
API_KEY = os.environ.get('GEMINI_API_KEY')

# Configure Google Gemini
if not API_KEY:
    st.error("Gemini API Key is not set. Please set the 'GEMINI_API_KEY' environment variable.")
    st.stop() # Stop the app if API key is missing

genai.configure(api_key=API_KEY)

# Initialize the Generative AI model (using gemini-2.0-flash)
# This model setup needs to be done once.
try:
    model = genai.GenerativeModel('gemini-2.0-flash')
except Exception as e:
    st.error(f"Failed to load Gemini model. Check API key or network connection: {e}")
    st.stop()


# Define the system prompt for the chatbot
SYSTEM_PROMPT = """
You are Sammy, a friendly and knowledgeable AI-powered chatbot designed to help students and staff members at the University of Information and Communication Technology (UICT) understand cybersecurity concepts. Your role is to provide clear, concise, and accurate explanations of cybersecurity topics, tools, and best practices in a way that is easy to understand for users with varying levels of expertise. You can answer questions about topics like phishing, malware, password security, network security, and data protection. Additionally, you can provide guidance on how to stay safe online and respond to common cybersecurity threats. Always maintain a helpful, approachable, and engaging tone. If a user’s question is unclear, ask for clarification to ensure your response is relevant and useful. Your knowledge is strictly limited to cybersecurity, and you should not respond to queries outside this domain. Always address the user by their name to make the conversation more personal and engaging.
"""

# Function to initialize or reset the chat session
def initialize_chat():
    # ALWAYS ensure 'messages' is initialized first, before appending to it.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 'chat_session_history' will be used to store the actual history for the LLM
    # This ensures the SYSTEM_PROMPT is sent only once at the start of a new session
    if "chat_session_history" not in st.session_state:
        # Start a new chat session with the system prompt
        st.session_state.chat_session_history = model.start_chat(history=[
            {"role": "user", "parts": [SYSTEM_PROMPT]},
            {"role": "model", "parts": ["Understood. I am ready to assist UICT students and staff with their cybersecurity questions."]}
        ])
        # Add the initial welcome message from the assistant to the display history
        # ONLY add this if messages is currently empty (i.e., a truly fresh start)
        if not st.session_state.messages: # Check if display messages list is empty
            st.session_state.messages.append({"role": "assistant", "content": "Welcome to Sammy, your friendly cybersecurity assistant! How can I help you stay safe online today?"})


# Function to display the chat history
def display_chat_history():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# --- New function to handle clearing the conversation ---
def clear_conversation():
    st.session_state.messages = [] # Clear display history
    # Re-initialize the LLM chat session to clear its context
    st.session_state.chat_session_history = model.start_chat(history=[
        {"role": "user", "parts": [SYSTEM_PROMPT]},
        {"role": "model", "parts": ["Understood. I am ready to assist UICT students and staff with their cybersecurity questions."]}
    ])
    # Re-add the initial welcome message for a fresh start
    st.session_state.messages.append({"role": "assistant", "content": "Welcome to Sammy, your friendly cybersecurity assistant! How can I help you stay safe online today?"})
    st.rerun()

# Function to add a message to the chat history (for display)
def add_message_to_display(role, content):
    st.session_state.messages.append({"role": role, "content": content})

# --- MOVED: Function to handle starting a new conversation (now globally accessible) ---
def start_new_conversation():
    st.session_state.messages = []  # Clear display messages
    # Re-initialize chat_session_history to clear LLM's context
    st.session_state.chat_session_history = model.start_chat(history=[
        {"role": "user", "parts": [SYSTEM_PROMPT]},
        {"role": "model", "parts": ["Understood. I am ready to assist UICT students and staff with their cybersecurity questions."]}
    ])
    st.session_state.messages.append({"role": "assistant", "content": "Conversation reset. Welcome back! How can I help you stay safe online today?"})
    st.rerun() # Use st.rerun() to immediately update the UI

# Streamlit app
def main():
    # Set page configuration
    st.set_page_config(
        page_title="UICT Cybersecurity Chatbot",
        page_icon="🔒",
        layout="centered",
    )

    # Custom CSS for styling
    st.markdown(
        """
        <style>

        .block-container {
            max-width: 800px;
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 1rem;
            padding-right: 1rem;
            margin-left: auto;
            margin-right: auto;
         }
        
        .stApp {
            background-color: #f0f0f0; /* Light gray background */
            font-family: "Inter", sans-serif; /* Use Inter font */
        }
        .stChatMessage {
            background-color: #ffffff; /* White chat bubbles */
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
        }
        .stChatMessage.user { /* Style for user messages */
            background-color: #e0f2f7; /* Light blue for user */
        }
        .stButton button {
            background-color: #007bff; /* Purple button */
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-weight: bold;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #0056b3; /* Darker purple on hover */
            color: black; /* Changed to black on hover */
        }
        .stTextInput label {
            font-size: 1.1em;
            font-weight: bold;
            color: #333;
        }
        .stTextInput input {
            background-color: #ffffff; /* White input box */
            border-radius: 10px;
            padding: 10px;
            border: 1px solid #ccc;
        }
        .stTextInput input:focus {
            border-color: #800080;
            box-shadow: 0 0 0 0.1rem rgba(128, 0, 128, 0.25);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Initialize chat session
    initialize_chat()

    # Logo (assuming 'assets/UICT_Logo.png' exists in your project structure)

    st.write("")
    logo_path = os.path.join(os.path.dirname(__file__), "assets", "UICT_Logo.png")
    if os.path.exists(logo_path):
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image(logo_path, width=300) # Adjusted width for better fit on various screens
    else:
        st.warning("UICT Logo not found at 'assets/UICT_Logo.png'. Please ensure the path is correct.")

    # --- Implement "Start new conversation" button ---
   # st.markdown("---")
    # if st.button("Start New Conversation", key="new_conversation_btn"):
      #  start_new_conversation()
    # st.markdown("---")

    # App title and description
    st.title("🔒 UICT Cybersecurity Chatbot")
    # This welcome message is now handled by initialize_chat to avoid duplicates
    # st.markdown("Welcome to **Sammy**, your friendly cybersecurity assistant! Type your questions below, and I'll help you stay safe online.")

    # Display chat history
    display_chat_history()

    # --- Phase 1, Part 1: Clear Call to Action & Contextual Guidance (Suggestion Buttons) ---
    st.markdown("---") # Visual separator for suggestions
    st.subheader("Quick Suggestions:")
    col_sug1, col_sug2, col_sug3 = st.columns(3)

    # Wrap the button logic in a function or simplify for readability,
    # ensuring that if a button is clicked, the app reruns.
    def handle_suggestion(suggestion_text):
        add_message_to_display("user", suggestion_text)
        with st.chat_message("assistant"):
            with st.spinner("Sammy is typing..."):
                try:
                    # Pass the suggestion text to the LLM chat session
                    response = st.session_state.chat_session_history.send_message(suggestion_text)
                    add_message_to_display("assistant", response.text)
                except Exception as e:
                    add_message_to_display("assistant", f"Sorry, I encountered an error. Please try again. Error: {e}")
        st.rerun() # Rerun to update history


    with col_sug1:
        if st.button("What is phishing?", key="suggest1_btn"):
            handle_suggestion("What is phishing?")
    with col_sug2:
        if st.button("Password tips", key="suggest2_btn"):
            handle_suggestion("Password tips")
    with col_sug3:
        if st.button("Ransomware definition", key="suggest3_btn"):
            handle_suggestion("Ransomware definition")
    st.markdown("---") # Visual separator

     # --- Implement "Start new conversation" button ---
    if st.button("Start New Conversation", key="new_conversation_btn"):
        start_new_conversation()


    # User input (main prompt area)
    # Phase 1, Part 1: Clear Call to Action (placeholder text)
    user_input = st.chat_input("Ask your cybersecurity question here...")

    if user_input:
        # Add user message to display history
        add_message_to_display("user", user_input)

        # Send user input to the chatbot
        with st.chat_message("assistant"):
            # --- Phase 1, Part 2: Visual Feedback (Chatbot Typing Indicator) ---
            with st.spinner("Sammy is typing..."):
                try:
                    response = st.session_state.chat_session_history.send_message(user_input)
                    add_message_to_display("assistant", response.text)
                except Exception as e:
                    add_message_to_display("assistant", f"Sorry, I encountered an error. Please try again. Error: {e}")

        # --- Phase 1, Part 3: Intuitive Conversation Flow (Auto-Scroll) ---
        # st.rerun() handles this naturally by re-rendering the updated history
        st.rerun()

# Run the Streamlit app
if __name__ == "__main__":
    main()
