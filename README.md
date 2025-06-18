# 🔒 UICT Cybersecurity Chatbot - Sammy

## Overview
Sammy is an AI-powered Cybersecurity Chatbot built with Streamlit and Google Gemini. Designed to enhance digital safety by providing UICT students and staff with accessible, real-time guidance on cyber threats and best practices.

## Table of Contents

![Sammy Chatbot Logo](assets/UICT_Logo.png) 
- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Features](#features)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Future Improvements (Roadmap)](#future-improvements-roadmap)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Introduction

Welcome to **Sammy**, the UICT Cybersecurity Chatbot! This project is an interactive, AI-powered assistant built to empower students and staff at the University of Information and Communication Technology (UICT) with readily accessible and accurate cybersecurity knowledge. Developed using Streamlit and leveraging the advanced capabilities of Google's Gemini Large Language Model, Sammy aims to enhance digital safety and awareness within the UICT community.

## Problem Statement

Students and staff within the community are constantly exposed to various online security dangers. These often show up as tricky online scams like phishing emails or fake messages that try to trick us into giving away our personal details.

We also deal with the risk of harmful software (malware) infecting our devices, including serious threats like ransomware, that can lock up our files. A major concern is also attempts to steal our login details or get unauthorized access to our accounts, or even the institution's official systems and sensitive data.

All these threats really put our personal online activities at risk and can disrupt the smooth digital operations and security of our institution.

## Features

Sammy, the UICT Cybersecurity Chatbot, offers a range of features designed for an intuitive and helpful user experience:

* **Conversational AI:** Powered by Google's Gemini Large Language Model, providing natural and intelligent responses to cybersecurity queries.
* **User-Friendly Interface:** Built with Streamlit, offering a clean, responsive, and easy-to-navigate chat environment.
* **Cybersecurity Q&A:** Answers questions on various topics including phishing, malware, password security, network safety, and data protection.
* **Contextual Suggestions:** Provides quick-access buttons for common cybersecurity questions to guide user interactions.
* **Real-time Visual Feedback:** Displays a "Sammy is typing..." indicator to inform users when the chatbot is processing a response.
* **Intuitive Chat Flow:** Automatically scrolls to the latest messages, ensuring a seamless conversation experience.
* **Clear Conversation Reset:** A "Start New Conversation" button allows users to easily clear the chat history and begin a new session.

## How It Works

The UICT Cybersecurity Chatbot operates on a client-server model, utilizing Streamlit for the front-end interface and Google's Gemini API for its intelligent core.

1.  **User Interaction:** Users interact with the chatbot via a web-based interface (Streamlit), typing questions or clicking on suggested topics.
2.  **Query Processing:** User queries, along with the conversation history, are sent to the chatbot's backend logic.
3.  **LLM Integration:** The backend sends these queries to the Google Gemini Large Language Model via its API.
4.  **Response Generation:** The Gemini LLM processes the input, generates a relevant cybersecurity response based on its training and the system prompt.
5.  **Display Output:** The chatbot's response is then displayed back to the user in the chat interface.

## Technologies Used

This project is built using the following key technologies:

* **Python:** The primary programming language used for all backend logic and application scripting.
* **Streamlit:** An open-source app framework used for building the interactive web-based user interface.
* **Google Gemini API:** Provides the Large Language Model (LLM) capabilities for conversational AI and intelligent response generation.
* **Pillow (PIL):** A Python Imaging Library used for handling image assets (e.g., loading the UICT logo).

## Installation & Setup

Follow these steps to get Sammy up and running on your local Linux machine:

### Prerequisites

* Python 3.8+
* `pip` (Python package installer)
* An active internet connection (required for LLM API access)
* A **Google Gemini API Key**. You can obtain one from the [Google AI Studio](https://aistudio.google.com/app/apikey).

### Steps

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Andrew235-art/An-LLM-Chatbot-For-Cybersecurity.git](https://github.com/your-username/An-LLM-Chatbot-For-Cybersecurity.git)
    cd An-LLM-chatbot-For-Cybersecurity
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv sammyVenv02
    source sammyVenv02/bin/activate
    ```

3.  **Install dependencies:**
    Create a `requirements.txt` file in your project's root directory with the following content:
    ```
    streamlit
    google-generativeai
    Pillow # Required for image handling, even if only used for logo display initially
    (Plus other extra dependencies downloaded automatically)...
    ```
    Then, install them:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set your Google Gemini API Key:**
    It's crucial to set your API key as an environment variable. Replace `YOUR_ACTUAL_GEMINI_API_KEY_HERE` with your key.
    ```bash
    export GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"
    ```
    *Note: For persistent local setup, you might consider adding this to your `~/.bashrc` or `~/.zshrc` file, then `source ~/.bashrc`.*

5.  **Run the Streamlit application:**
    ```bash
    streamlit run chatbotaiv3.py
    ```

    Your browser should automatically open to the Streamlit app.

## Usage

Once the application is running, you can interact with Sammy in a few ways:

* **Type your questions:** Use the input box at the bottom to type your cybersecurity questions.
* **Use Quick Suggestions:** Click on the provided buttons like "What is phishing?" or "Password tips" to quickly ask common questions.
* **Start a New Conversation:** Click the "Start New Conversation" button to clear the chat history and begin a fresh interaction.

## Future Improvements (Roadmap)

The UICT Cybersecurity Chatbot is a growing project with exciting possibilities for future enhancements:

* **Image Analysis (OCR):**
    * Allow users to upload images (screenshots) for text extraction and cybersecurity analysis by the chatbot.
* **Real-time Threat Intelligence Integration:**
    * Connect with external threat intelligence feeds to provide up-to-the-minute information on emerging cyber risks.
* **Interactive Learning Modules:**
    * Develop features like quizzes, simulated scenarios (e.g., phishing tests), or gamified content to enhance cybersecurity education.
* **Streamlined Incident Reporting:**
    * Enable users to report cybersecurity incidents directly through the chatbot, potentially integrating with existing IT support systems.
* **Robust Analytics & Feedback Loop:**
    * Implement a dashboard to monitor chatbot performance, user engagement, and common query patterns to guide continuous improvement.

## Project Structure
```
.
├── chatbotaiv3.py  # Main Streamlit application file
├── requirements.txt # Python dependencies
└── assets/
└── UICT_Logo.png # UICT logo image (ensure this path is correct)
```
## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## Authors

* **Bisaso Andrew** - *Initial Development & Lead* - [@Andrew235-art](https://github.com/Andrew235-art)
* Sseninde Joshua -  *Initial Development & Project Contributor*
* Nakalema Sophie - *Documentation & Initial Development* 
* Nakato Florence R M - *Documentation & Initial Development* 
* Ocheger Emmanuel - *Project Contibutor & Initial Development* 

## License

MIT License

## Acknowledgements

We extend our sincere gratitude to the following for their invaluable contributions and support to this project:

* **Google Gemini API:** For powering the sophisticated conversational intelligence and natural language understanding capabilities of the chatbot.
* **Streamlit:** For providing an incredibly intuitive and efficient open-source framework that enabled the rapid development and deployment of the web-based user interface.
* **UICT Community:** For serving as the inspiration and target users for this project, highlighting the critical need for enhanced cybersecurity awareness within the institution.

---


