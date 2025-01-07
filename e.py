import requests
ELEVEN_LABS_API_KEY = ""

# Function to list available voices
def list_voices():
    url = "https://api.elevenlabs.io/v1/voices"
    headers = {
        "xi-api-key": ELEVEN_LABS_API_KEY
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        voices = response.json()["voices"]
        print("Available Voices:")
        for voice in voices:
            print(f"Voice ID: {voice['voice_id']}, Name: {voice['name']}")
        return voices
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []

def convert_text_to_speech(text, voice="your_valid_voice_id"):
    """Convert text to speech using Eleven Labs API."""
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
    print("Fetching available voices...")
    voices = list_voices()

    if voices:
        selected_voice_id = voices[0]['voice_id']
        print(f"Using Voice ID: {selected_voice_id}")

        static_text = "Hello! This is a test of Eleven Labs text-to-speech functionality."

        print("Converting text to speech using Eleven Labs...")
        convert_text_to_speech(static_text, voice=selected_voice_id)
    else:
        print("No voices available. Please check your Eleven Labs account.")
