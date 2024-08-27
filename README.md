
Replace `your_news_api_key` and `your_openai_api_key` with your actual API keys.

## Usage

1. **Run the Flask application**:
 ```bash
 python app.py
 ```

2. **Access the web interface**:

Open your web browser and go to `http://127.0.0.1:5000/`.

3. **Interact with Nova**:

Use the text input or voice commands to interact with Nova. Examples of commands include:

- "Open Google"
- "Search Python tutorials"
- "Play Imagine by John Lennon"
- "What's the time?"
- "Show me the latest news"

## Configuration

- **Logging**: The application uses Python’s built-in logging module for error and debug logging. Adjust the logging level as needed.
- **API Keys**: Make sure to replace the placeholders with your actual API keys for OpenAI and NewsAPI.
- **Music Library**: Modify `musicLibrary.py` to add or update songs and their URLs.

## Notes

- Ensure you have a stable internet connection, as the application relies on several web-based services.
- Adjust your microphone and speaker settings to improve the accuracy of speech recognition and text-to-speech functionalities.
- This application requires access to your microphone and speakers for full functionality.

## Contributing

We welcome contributions! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for the GPT-3.5-turbo model.
- NewsAPI for the latest news updates.
- Python community for the wonderful libraries that made this project possible.
