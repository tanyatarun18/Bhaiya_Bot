Bhaiya Bot 🤖 - Your Personal AI Voice Tutor
Live Demo: bhaiyabot.netlify.app

Bhaiya Bot is an intelligent, conversational AI voice tutor designed to provide personalized academic help to students of all levels, from nursery school to those preparing for competitive exams like JEE and NEET.

🌟 About The Project
The inspiration for Bhaiya Bot came from watching my own brother prepare for his NEET exams. He often had specific questions but no one was available at that moment to provide a clear, understandable explanation. I realized that millions of students face this same challenge. They don't just need an answer; they need an explanation tailored to their level of understanding.

Bhaiya Bot was built to be that "always-on" study companion—a knowledgeable older brother (a "Bhaiya") who can explain anything, anytime, in a way that truly makes sense.

Key Features
🎤 Voice & Text Input: Ask questions naturally by speaking or typing.

🧠 Dynamic Expertise Levels: The bot adapts its teaching style and answer complexity based on the user's selected academic level (from Nursery to JEE/NEET).

🔊 Text-to-Speech Output: Hear the answers spoken aloud for a truly conversational learning experience.

🛑 Stop Speaking Functionality: Full control to stop the bot's voice output at any time.

✨ Modern & Professional UI: A sleek, responsive, and visually appealing interface built with a dark theme and "glassmorphism" effects.

🚀 Live on the Web: Fully deployed and accessible to anyone with a web browser.

🛠️ How It's Built: The Tech Stack
This project is a full-stack web application combining a Python backend with a modern JavaScript frontend.

Backend:

Framework: Flask

AI: Google Gemini API (gemini-1.5-flash model)

Server: Gunicorn

Frontend:

Languages: HTML, CSS, JavaScript (Vanilla)

Styling: Tailwind CSS

Voice I/O: Web Speech API (SpeechRecognition & SpeechSynthesis)

Animation: Lottie

Deployment:

Backend: Render

Frontend: Netlify

🚀 Getting Started (Running Locally)
To get a local copy up and running, follow these simple steps.

Prerequisites
Python 3.8+ installed

A Google Gemini API Key

Installation & Setup
Clone the repo:

git clone https://github.com/YOUR_USERNAME/bhaiya-bot-hackathon.git
cd bhaiya-bot-hackathon

Create and activate a virtual environment:

# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install the required packages:

pip install -r requirements.txt

Set up your API Key:

Create a file named .env in the root directory.

Add your API key to it like this: GOOGLE_API_KEY=YOUR_API_KEY_HERE

Run the server:

flask run --host=0.0.0.0

Open the website:

Navigate to the templates folder and open the index.html file in your browser.

Important: For local testing, you'll need to change the API_URL in index.html from the Render link back to http://127.0.0.1:5000/api/ask.
