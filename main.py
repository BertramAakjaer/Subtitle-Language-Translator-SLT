#   External libaries used in the following scipt
import streamlit as st
from io import StringIO

#   Modules from subfolders
from sub_functions.translation_function import translate_text

#*********************************************************************
#   Function to display the interactable UI can be found under here !!
#*********************************************************************


#   Streamlit UI
def main() -> None:

    st.title("Subtitle Language Translator")

    # File Uploader
    uploaded_file = st.file_uploader("Choose a subtitle (SubRip) file", type=["srt"])

    if uploaded_file is not None:
        # Read File Contents
        file_contents = uploaded_file.read().decode("utf-8")  # Decode bytes to text

        # Display File Contents
        st.subheader("File Contents:")
        st.text_area(label="", value=file_contents, height=150)
        
        lines_seperated = file_contents.replace('\r', '').split('\n')
        
        new_file_name = st.text_input("New file name (.srt will be added by program)")
        new_language = st.selectbox("Choose new language", ["Pick one here!!","da", "de", "en", "es", "fr"])
        
        if st.button("Start translation!"):
            if new_file_name != '' and new_language != "Pick one here!!":
                
                progress_bar = st.progress(0)
                
                time_text = st.empty()
                time_text.text(f"Calculating time left...")
                
                curr_translation = st.empty()
                curr_translation.text("Waiting for translation...")
                translate_text(lines_seperated, new_language, time_text, curr_translation, progress_bar, new_file_name)
            else:
                st.warning("Check the options over here ^")


if __name__ == "__main__":
    main()