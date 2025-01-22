from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import ttk, messagebox
def translate_text(text, src_lang='en', dest_lang='es'):
    try:
        return GoogleTranslator(source=src_lang, target=dest_lang).translate(text)
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {e}")
        return None
def translate_action():
    text = input_text.get("1.0", tk.END).strip()
    src_lang = lang_code_map.get(source_lang.get(), 'en')
    dest_lang = lang_code_map.get(target_lang.get(), 'es')
    if not text:
        messagebox.showerror("Input Error", "Please enter text to translate.")
        return
    translated_text = translate_text(text, src_lang, dest_lang)
    if translated_text:
        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_text)
        output_text.config(state="disabled")
def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.config(state="disabled")
def create_gui():
    global input_text, output_text, source_lang, target_lang
    root = tk.Tk()
    root.title("Language Translator")
    root.geometry("600x500")
    root.resizable(False, False)
    # Styling
    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12))
    style.configure("TCombobox", font=("Arial", 12))
    root.configure(bg="#f0f0f0")  # Set background color
    # Title
    tk.Label(root, text="Language Translator", font=("Arial", 18, "bold"), pady=10, bg="#f0f0f0", fg="#333").pack()
    # Frame for input text
    input_frame = tk.Frame(root, bg="#f0f0f0")
    input_frame.pack(pady=10, padx=10, fill="x")
    tk.Label(input_frame, text="Enter Text:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=0, column=0, sticky="w")
    input_text = tk.Text(input_frame, height=6, width=60, wrap="word", font=("Arial", 12), bg="#ffffff", fg="#000", bd=2, relief="solid")
    input_text.grid(row=1, column=0, columnspan=2, pady=5)
    # Frame for language selection
    lang_frame = tk.Frame(root, bg="#f0f0f0")
    lang_frame.pack(pady=10, padx=10, fill="x")
    tk.Label(lang_frame, text="Source Language:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=0, column=0, sticky="w", padx=5)
    source_lang = ttk.Combobox(lang_frame, values=list(lang_code_map.keys()), state="readonly", width=20)
    source_lang.set("English")
    source_lang.grid(row=0, column=1, padx=5)
    tk.Label(lang_frame, text="Target Language:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=1, column=0, sticky="w", padx=5)
    target_lang = ttk.Combobox(lang_frame, values=list(lang_code_map.keys()), state="readonly", width=20)
    target_lang.set("Spanish")
    target_lang.grid(row=1, column=1, padx=5)
    # Frame for buttons
    button_frame = tk.Frame(root, bg="#f0f0f0")
    button_frame.pack(pady=10)
    translate_button = ttk.Button(button_frame, text="Translate", command=translate_action)
    translate_button.grid(row=0, column=0, padx=10)
    clear_button = ttk.Button(button_frame, text="Clear", command=clear_text)
    clear_button.grid(row=0, column=1, padx=10)
    # Frame for output text
    output_frame = tk.Frame(root, bg="#f0f0f0")
    output_frame.pack(pady=10, padx=10, fill="x")
    tk.Label(output_frame, text="Translated Text:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=0, column=0, sticky="w")
    output_text = tk.Text(output_frame, height=6, width=60, wrap="word", font=("Arial", 12), bg="#e8f4ff", fg="#000", state="disabled", bd=2, relief="solid")
    output_text.grid(row=1, column=0, pady=5)
    # Run the application
    root.mainloop()
# Create an instance of GoogleTranslator and fetch supported languages
translator = GoogleTranslator(source='auto', target='en')  # Instance required
supported_languages = translator.get_supported_languages(as_dict=False)
lang_code_map = {lang.title(): lang.lower() for lang in supported_languages}
if __name__ == "__main__":
    create_gui()
