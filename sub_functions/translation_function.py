from googletrans import Translator
from datetime import datetime
import streamlit as st
import os

# Function to translate a SubRip file
def translate_text(content, 
                   new_language, 
                   time_text, 
                   curr_translation,
                   progress_bar, 
                   new_file_name) -> None:
  
  # Variables to be used in function
  just_started_new = False
  curr_subtitle = 1

  # Arrays for pasting timestamps and lines that should be translated
  lines_to_translate = []
  timestamps = []
  
  # Debug mode for shorter translation times
  debug_mode = False
  
  if debug_mode:
    rotation_count = 0

  # For loop to "clean" incomming text into text to translate and timestamps
  for line in content:
    # Writing to user interface
    time_text.text("Calculating time left...")
    curr_translation.text("Sorting files...")
    
    # Stop early in debug mode
    if debug_mode:
      if rotation_count >= 150:
        break
      else:
        rotation_count += 1
    
    ##############################
    # Cleanup of the actual text #
    ##############################
    
    if just_started_new:
      timestamps.append(line)
      just_started_new = False
      continue
    
    if line == '':
      continue
    
    if line.isdigit(): 
      if int(line) == curr_subtitle:
        just_started_new = True
        curr_subtitle += 1
        continue
      
    if (len(lines_to_translate) == curr_subtitle - 2) or (len(lines_to_translate) == 0):
      lines_to_translate.append(line)
    else:
      lines_to_translate[-1] += ('\n' + str(line))

  # Starting translator used in the googletrans libary
  translator = Translator()
  
  translated_lines = []

  curr_translation.text("Translation started...")
  start_timecode = datetime.now().strftime('%H:%M:%S.%f')
  
  # Loop for translating every line in array
  for i, to_translation in enumerate(lines_to_translate):
    progress_translation = (i + 1)/len(lines_to_translate)
    progress_bar.progress(progress_translation)
    
    # Calculating remaining time
    if to_translation != lines_to_translate[0]:
            time_estimate = datetime.now().strftime('%H:%M:%S.%f')
            
            curr_used_time = (time_to_float(time_estimate) - time_to_float(start_timecode))
            time_left_guess = str(100/(progress_translation * 100) * curr_used_time - curr_used_time)
            
            time_text_seconds = time_left_guess[:5] + " Estimated seconds to done!"
            time_text_minutes = str(float(time_left_guess[:5])/60)[:5] + " Minutes!"
            
            time_text.text(time_text_seconds + " / " + time_text_minutes)
    
    # Translating string with libary
    translation = translator.translate(to_translation, dest=new_language)
    
    # Printing current translation to user
    curr_translation.text(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    
    translated_lines.append(translation.text)
  
  
  ###############################
  # Writing translation to file #
  ###############################
  translation_file = open(r"output/{}.srt".format(new_file_name), "w", encoding='utf8')
  
  for i, timestamp in enumerate(timestamps):
    # Joining different parts of information to single string
    temp_list = [str(i + 1), timestamp, translated_lines[i], '\n']
    translation_file.write('\n'.join(temp_list))

  translation_file.close()
  
  st.write("File opened in explorer !!")
  os.startfile(os.path.relpath("output"))

# Calculate a string in the format "%H:%M:%S.%f" to a float of seconds
def time_to_float(time_str):
    listen = time_str.split(':')
    seconds_time = float(listen[2][:-4]) + 60 * (int(listen[1]) + 60 * int(listen[0]))
    return seconds_time