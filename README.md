🦾 Ultron - Your Voice Assistant
Ultron is a Python-based voice assistant that responds to voice commands for opening popular websites and fetching real-time weather information using OpenWeatherMap API. Just say "Ultron" to activate it, and give a command!

🛠 Features
🎙️ Voice Activation: Say "Ultron" to wake up the assistant.

🌐 Open Websites: Commands like "open Google", "open YouTube", etc.

☁️ Get Weather Info: Say "weather" and then your city name to hear current conditions.

🔊 Text-to-Speech: Uses pyttsx3 to speak responses aloud.

📦 Requirements
Install the dependencies using pip:
pip install SpeechRecognition
pip install pyttsx3
pip install requests
pip install pyaudio

⚠️ pyaudio can be tricky to install on some systems. On Windows, use:
pip install pipwin
pipwin install pyaudio

🔑 Setup
Replace the placeholder API key in the script with your actual OpenWeatherMap API key:
api_key = "YOUR_API_KEY_HERE"


🚀 How to Run
Run the script:
python ultron.py

Then, speak the wake word:
Ultron
Follow up with commands like:

"Open Google"
"Open YouTube"
"Weather"

🧠 Future Improvements
Add more commands (play music, send emails, etc.)
Improve speech recognition accuracy
Integrate with ChatGPT or other AI models for smarter responses

👤 Author
Shubhadeep Nath
LinkedIn | GitHub
