from googletrans import Translator
from datetime import datetime
import streamlit as st
import os

def translate_text(content, 
                   new_language, 
                   time_text, 
                   curr_translation,
                   progress_bar, 
                   new_file_name) -> None:

  just_started_new = False
  curr_subtitle = 1

  lines_to_translate = []
  timestamps = []

  rotation_count = 0

  for line in content:
    time_text.text("Calculating time left...")
    curr_translation.text("Sorting files...")
    if rotation_count >= 150:
      break
    rotation_count += 1
    
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



  translator = Translator()
  translated_lines = []

  curr_translation.text("Translation started...")
  start_timecode = datetime.now().strftime('%H:%M:%S.%f')
  
  for i, to_translation in enumerate(lines_to_translate):
    progress_translation = (i + 1)/len(lines_to_translate)
    progress_bar.progress(progress_translation)
    
    if to_translation != lines_to_translate[0]:
            time_estimate = datetime.now().strftime('%H:%M:%S.%f')
            
            curr_used_time = (time_to_float(time_estimate) - time_to_float(start_timecode))
            time_left_guess = str(100/(progress_translation * 100) * curr_used_time - curr_used_time)
            
            time_text_seconds = time_left_guess[:5] + " Estimated seconds to done!"
            time_text_minutes = str(float(time_left_guess[:5])/60)[:5] + " Minutes!"
            
            time_text.text(time_text_seconds + " / " + time_text_minutes)
    
    translation = translator.translate(to_translation, dest=new_language)
      
    curr_translation.text(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
      
    translated_lines.append(translation.text)
      
  translation_file = open(r"output/{}.srt".format(new_file_name), "w", encoding='utf8')


  for i, timestamp in enumerate(timestamps):
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