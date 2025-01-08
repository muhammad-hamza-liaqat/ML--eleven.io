import os
from dotenv import load_dotenv
load_dotenv()
from elevenlabs import ElevenLabs


ELEVENLABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

SAVING_DIR = "soundEffects"

def create_audio_dir():
    if not os.path.exists(SAVING_DIR):
        os.makedirs(SAVING_DIR)

def generate_unique_filename(prompt):
    base_filename = prompt.replace(" ", "_").lower()
    counter = 1
    while True:
        filename = f"{base_filename}_{counter}.mp3"
        filepath = os.path.join(SAVING_DIR, filename)
        if not os.path.exists(filepath):
            return filepath
        counter += 1


def generate_sound_effect(prompt):

    try:
        audio_generator = client.text_to_sound_effects.convert(text=prompt)

        audio_content = b"".join(audio_generator)

        output_audio = generate_unique_filename(prompt)

        with open(output_audio, "wb") as f:
            f.write(audio_content)
        print(f"Generated SFX saved as {output_audio}")
        return output_audio

    except Exception as e:
        print(f"Error generating SFX with ElevenLabs: {e}")
        return None


if __name__ == "__main__":
    create_audio_dir()

    user_prompt = input("Enter the sound effect prompt: ")

    print("Generating SFX with ElevenLabs...")
    sfx_audio = generate_sound_effect(user_prompt)

    if sfx_audio:
        print(f"SFX successfully generated: {sfx_audio}")
    else:
        print("Failed to generate SFX.")
