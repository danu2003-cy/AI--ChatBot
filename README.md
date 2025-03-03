# Cute ChatBot

A simple chatbot application built with Tkinter and Hugging Face's Inference API, designed for fun and to experiment with chatbot interactions.

## Features
- User-friendly graphical interface using Tkinter
- Scrolled text area to display chat history
- Real-time chatbot responses powered by Hugging Face's `Llama-3.1-70B-Instruct`
- Easy-to-use input field and send button

## Requirements
Ensure you have the following installed before running the project:
- Python 3.x
- Required dependencies:
  
  ```sh
  pip install tkinter huggingface_hub
  ```

## Setup and Usage
1. Clone this repository or copy the script.
2. Ensure you have a valid Hugging Face API key and update `api_key` in the script.
3. Run the script:
   
   ```sh
   python chatbot.py
   ```
4. Type messages into the input field and interact with the chatbot.

## Files
- `chatbot.py`: Main script for the chatbot interface and logic.

## Future Improvements
- Enhance UI design with better styling.
- Add support for multiple chatbot models.
- Implement message persistence and logging.

## Disclaimer
This chatbot is built for experimentation and fun. The accuracy and responses depend on the model used from Hugging Face's Inference API.

## License
This project is open-source and free to use.
