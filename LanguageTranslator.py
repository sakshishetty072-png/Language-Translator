from tkinter import *
import googletrans
from textblob import TextBlob
from tkinter import ttk, messagebox

root = Tk()
root.title('Language Translator')
root.geometry("880x300")

# Function to translate text
def translate_it():
    try:
        # Clear previous translations
        translated_text.delete(1.0, END)

        # Get the source and destination languages
        from_language = original_combo.get()
        to_language = translated_combo.get()

        # Get corresponding language keys
        from_lang_key = [key for key, value in languages.items() if value == from_language][0]
        to_lang_key = [key for key, value in languages.items() if value == to_language][0]

        # Get the input text
        words = TextBlob(original_text.get(1.0, END))

        # Translate text
        translated_words = words.translate(to=to_lang_key)

        # Display translated text
        translated_text.insert(1.0, translated_words)

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Function to clear text fields
def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

# Get language dictionary from googletrans
languages = googletrans.LANGUAGES
language_list = list(languages.values())

# Text input fields
original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(root, text="Translate!", font=("Helvetica", 24), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20, padx=10)

# Dropdown menus for languages
original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)  # Set default language
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(26)  # Set default translated language
translated_combo.grid(row=1, column=2)

# Clear button
clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()
