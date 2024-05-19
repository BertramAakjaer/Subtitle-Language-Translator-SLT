import tkinter as tk
import customtkinter as cTk
from tkinter import filedialog

class App(cTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x600")
        self.title("Subtitle(.srt) Language Translator")
        self.resizable(True, False)
   
        def select_file():
            # Use filedialog.askopenfilename to open the file selection dialog
            filename = filedialog.askopenfilename(
                title="Select a file !!",
                filetypes=[("SRT (SubRip) Subtitles", "*.srt")]  # You can customize filetypes here
            )
            
            # Check if a file was selected
            if filename:
                # Process the selected filename (e.g., display it in a label)
                choosen_file = filename
                
                
                self.label1.configure(text=str(filename).split("/")[-1])
        
        def start_translation():
                print(self.progressbar.get())
                self.progressbar.step()
                print("coice is = " + str(self.combobox_var.get()))

        # Use CTkButton instead of tkinter Button
        self.button = cTk.CTkButton(self, text="Start translation !!", command=select_file)
        self.button.place(relx=0.5, rely=0.5, anchor=cTk.CENTER)
        
        self.file_button = cTk.CTkButton(self, text="Choose file !!", command=select_file)
        self.file_button.place(relx=0.5, rely=0.1, anchor=cTk.CENTER)

        self.label1 = cTk.CTkLabel(self, text="A file hasn't been choosen yet", fg_color="transparent", text_color="black")
        self.label1.place(relx=0.5, rely=0.05, anchor=cTk.CENTER)

        self.progressbar = cTk.CTkProgressBar(self, orientation="horizontal", height=30, width=350)
        self.progressbar.set(0)
        self.progressbar.place(relx=0.5, rely=0.75, anchor=cTk.CENTER)


        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)
        
        self.combobox_var = cTk.StringVar(value="Choose language")
        self.combobox = cTk.CTkComboBox(self, values=["da", "de", "en", "es", "fr"], command=combobox_callback, variable=self.combobox_var)
        self.combobox_var.set("Choose language")
        self.combobox.place(relx=0.5, rely=0.25, anchor=cTk.CENTER)

        self.entry = cTk.CTkEntry(self, placeholder_text="New File Name...")
        self.entry.place(relx=0.5, rely=0.35, anchor=cTk.CENTER)
        
        self.label = cTk.CTkLabel(self, text="Translation not started", fg_color="transparent", text_color="black")
        self.label.place(relx=0.5, rely=0.8, anchor=cTk.CENTER)

def main():
    cTk.set_appearance_mode("System")  # Modes: system (default), light, dark
    cTk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    choosen_file = ""

    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()