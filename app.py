import tkinter as tk
from tkinter import scrolledtext
from huggingface_hub import InferenceClient

# Initialize Hugging Face API client
client = InferenceClient(
    provider="sambanova",
    api_key="YOUR_API"
)

def send_message():
    user_input = user_entry.get()
    if not user_input.strip():
        return
    
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    user_entry.delete(0, tk.END)
    
    messages = [{"role": "user", "content": user_input}]
    try:
        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.1-70B-Instruct", 
            messages=messages, 
            max_tokens=500,
        )
        bot_response = completion.choices[0].message["content"]
    except Exception as e:
        bot_response = "Error: " + str(e)
    
    chat_history.insert(tk.END, "Bot: " + bot_response + "\n")
    chat_history.yview(tk.END)

# Create main application window
root = tk.Tk()
root.title("Interview Suite - Cute chatBot")
root.geometry("500x400")

# Chat history display
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
chat_history.pack(pady=10)

# User input field
user_entry = tk.Entry(root, width=50)
user_entry.pack(pady=5)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Run the application
root.mainloop()