import requests
import os
from dotenv import load_dotenv
load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")
print(OPENAI_API_KEY,ELEVEN_LABS_API_KEY, "from enviormental variables" )

def get_chatgpt_response(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo", 
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"ChatGPT Error: {response.status_code}, {response.text}")
        return None

# Eleven Labs Function
def convert_text_to_speech(text, voice="cjVigY5qzO86Huf0OWal"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice}"
    headers = {
        "xi-api-key": ELEVEN_LABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        audio_file = "output_audio.mp3"
        with open(audio_file, "wb") as f:
            f.write(response.content)
        print(f"Audio saved as {audio_file}")
    else:
        print(f"Eleven Labs Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")

    print("Fetching response from ChatGPT...")
    chatgpt_response = get_chatgpt_response(prompt)

    if chatgpt_response:
        print(f"ChatGPT Response: {chatgpt_response}")

        print("Converting text to speech using Eleven Labs...")
        convert_text_to_speech(chatgpt_response)