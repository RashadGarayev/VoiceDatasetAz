from faster_whisper import WhisperModel
from pydub import AudioSegment
import os,sys,re
import csv
import string
import digitpunc
model_size = "large-v2"
output_file_path = "corpora.txt"
model = WhisperModel(model_size, device="cpu", compute_type="int8")
audio_files = [f for f in os.listdir(r"/home/user/Downloads/audio") if f.endswith('.mp3')]
i = 0
# Open the output file in append mode outside the loop
with open(output_file_path, 'a', encoding='utf-8') as output_file:
    for audio_file in audio_files:
        audio_file_path = os.path.join(r"/home/user/Downloads/audio", audio_file)
        result = model.transcribe(audio_file_path)
        segments, info = model.transcribe(audio_file_path)

        for segment in segments:
            transcribed_text = segment.text.lower()
            transcribed_text = digitpunc.remove_punc_digits(transcribed_text)
            modified_text = digitpunc.replace_digits_with_words(transcribed_text)

            print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
            
            # Write the modified text to the output file
            output_file.write(modified_text + '\n')
            i += 1

print(f"Total {i} segments written to corpora.txt.")
