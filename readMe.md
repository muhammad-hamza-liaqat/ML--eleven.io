# Eleven Labs + ChatGPT Integration

This project integrates **ChatGPT** for generating text responses and **Eleven Labs** for converting those responses into speech. The workflow is as follows:

1. Enter a prompt into the script.
2. The script sends the prompt to ChatGPT (via OpenAI API).
3. ChatGPT generates a response.
4. The response is sent to Eleven Labs (via Eleven Labs API) to generate a voice output.
5. The resulting audio is saved as an MP3 file in the project directory.

## Prerequisites

- Python 3.6+
- API keys for:
  - **OpenAI**: To access the ChatGPT API.
  - **Eleven Labs**: To use the Eleven Labs text-to-speech API.

## Setup

1. Clone this repository or download the script file.

   ```bash
   git clone https://github.com/your-repo/eleven-labs-chatgpt.git
   cd eleven-labs-chatgpt
   ```

2. Install the required Python libraries:

   ```bash
   pip install requests
   ```

3. Add your API keys to the script:

   - Open `script.py` and replace the placeholders:

     ```python
     OPENAI_API_KEY = "your-openai-api-key"
     ELEVEN_LABS_API_KEY = "your-eleven-labs-api-key"
     ```

## Usage

1. Run the script:

   ```bash
   python script.py
   ```

2. Enter your prompt when prompted:

   ```
   Enter your prompt: What is artificial intelligence?
   ```

3. The script will:

   - Generate a response using ChatGPT.
   - Convert the response into speech using Eleven Labs.

4. Check the output:
   - The response will be displayed in the terminal.
   - An audio file named `output_audio.mp3` will be saved in the same directory.

## Example Workflow

1. **Input Prompt:**

   ```
   Enter your prompt: What is artificial intelligence?
   ```

2. **ChatGPT Response:**

   ```
   Artificial intelligence refers to the simulation of human intelligence in machines that are designed to think and learn.
   ```

3. **Generated Audio:**
   - Saved as `output_audio.mp3`.
   - You can play the file using any media player.

## Error Handling

- If no response is generated from ChatGPT, check your OpenAI API key.
- If the Eleven Labs text-to-speech conversion fails, ensure the voice ID and API key are valid.

## Notes

- Make sure your Eleven Labs account has access to the desired voice ID.
- The default voice ID used is `cjVigY5qzO86Huf0OWal` (Eric). You can change this by modifying the `voice` parameter in the script.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.
