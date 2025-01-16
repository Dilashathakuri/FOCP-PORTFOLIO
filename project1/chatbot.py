import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext
import random
import re

class EnhancedChatbot:
    def __init__(self):
        # Download required NLTK data
        try:
            nltk.download('punkt', quiet=True)
            nltk.download('averaged_perceptron_tagger', quiet=True)
            nltk.download('wordnet', quiet=True)
            nltk.download('stopwords', quiet=True)
            self.stop_words = set(stopwords.words('english'))
        except Exception as e:
            print(f"Warning: NLTK data download failed: {e}")
            self.stop_words = set()  

        self.lemmatizer = WordNetLemmatizer()
        
        # Knowledge base
        self.knowledge_base = {
            "greetings": {
                "patterns": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"],
                "responses": [
                    "Hello! How can I assist you today?",
                    "Hi there! What's on your mind?",
                    "Greetings! How may I help you?"
                ]
            },
            "farewell": {
                "patterns": ["bye", "goodbye", "see you", "quit", "exit", "cya"],
                "responses": [
                    "Goodbye! Have a great day!",
                    "See you later! Take care!",
                    "Farewell! It was nice chatting with you!"
                ]
            },
            "general": {
                "patterns": ["what can you do", "help", "features", "capabilities"],
                "responses": [
                    "I can help you with:\n- General knowledge about science and technology\n- Basic calculations\n- Time-related queries\n- Context-aware conversations",
                    "My capabilities include answering questions about science and technology, performing calculations, and engaging in context-aware discussions."
                ]
            }
        }

        self.context = {"current_topic": None, "conversation_history": []}

    def preprocess_text(self, text):
        try:
            tokens = word_tokenize(text.lower())
            tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words and token.isalnum()]
            return tokens
        except Exception as e:
            print(f"Error in text preprocessing: {e}")
            return text.lower().split()

    def generate_response(self, user_input):
        tokens = self.preprocess_text(user_input)
        for intent, data in self.knowledge_base.items():
            if any(pattern in user_input.lower() for pattern in data["patterns"]):
                response = random.choice(data["responses"])
                self.context["conversation_history"].append(("bot", response))
                return response

        if "time" in tokens:
            return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

        if any(math_word in tokens for math_word in ["calculate", "solve", "compute"]):
            return self.handle_math(user_input)

        return "I'm sorry, I didn't understand that. Could you rephrase your question?"

    def handle_math(self, expression):
        try:
            math_expression = re.findall(r'[\d+\-*/().\s]+', expression)
            if math_expression:
                safe_expression = ''.join(math_expression)
                if all(c in '0123456789+-*/.() ' for c in safe_expression):
                    result = eval(safe_expression)
                    return f"The result is: {result}"
            return "I couldn't process that calculation. Please use numbers and operators only."
        except Exception as e:
            return f"Error in calculation: {e}"

class EnhancedChatbotGUI:
    def __init__(self):
        self.chatbot = EnhancedChatbot()
        
        self.app = tk.Tk()
        self.app.title("Enhanced Local Chatbot")
        self.app.geometry("600x500")
        
        self.chat_log = scrolledtext.ScrolledText(self.app, wrap=tk.WORD, state=tk.DISABLED, width=70, height=25, font=("Arial", 10))
        self.chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.user_entry = tk.Entry(self.app, width=50, font=("Arial", 12))
        self.user_entry.grid(row=1, column=0, padx=10, pady=10)
        self.user_entry.bind("<Return>", lambda e: self.send_message())
        
        self.send_button = tk.Button(self.app, text="Send", command=self.send_message, width=10, font=("Arial", 10))
        self.send_button.grid(row=1, column=1, padx=10, pady=10)
        
        self.display_message("Bot", "Hello! I'm an enhanced chatbot. How can I assist you today?")

    def display_message(self, sender, message):
        self.chat_log.config(state=tk.NORMAL)
        self.chat_log.insert(tk.END, f"{sender}: {message}\n")
        self.chat_log.config(state=tk.DISABLED)
        self.chat_log.yview(tk.END)

    def send_message(self):
        user_input = self.user_entry.get().strip()
        if not user_input:
            return
        self.display_message("You", user_input)
        self.user_entry.delete(0, tk.END)

        bot_response = self.chatbot.generate_response(user_input)
        self.display_message("Bot", bot_response)

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    gui = EnhancedChatbotGUI()
    gui.run()
