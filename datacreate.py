from faster_whisper import WhisperModel
from pydub import AudioSegment
import os,sys,re,csv
from helper.digitpunc import remove_punc_digits,replace_digits_with_words

model_size = "large-v2"
output_dir = "clips"
csv_file = r'train'
header = ['path', 'filesize', 'transcript']
data = []
wav_directory = "clips"

# Run on GPU with FP16
#model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
#model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
model = WhisperModel(model_size, device="cpu", compute_type="int8")
audio_files = [f for f in os.listdir(r"/home/user/Downloads/audio") if f.endswith('.mp3')]
i=0
for audio_file in audio_files:
    audio_file_path = os.path.join(r"/home/user/Downloads/audio", audio_file)
    result = model.transcribe(audio_file_path)
    segments, info = model.transcribe(audio_file_path)
    audio = AudioSegment.from_mp3(audio_file_path)
    for segment in segments:
        # Calculate the segment duration in milliseconds
         # Replace with the actual transcribed text
        segment_audio = audio[segment.start*1000: segment.end*1000]
        segment_audio = segment_audio.set_channels(1)
        segment_audio = segment_audio.set_frame_rate(16000)
        # Define the output file path
        output_file_path = f"{output_dir}/common_voice_az_{i}.wav"
        # Export the segment as a WAV file
        segment_audio.export(output_file_path, format="wav")

        transcribed_text = segment.text
        transcribed_text = transcribed_text.lower()
        #pattern = r'[,"&^0-9]'
        transcribed_text = remove_punc_digits(transcribed_text)
        # Use the re.sub() function to replace the unwanted characters (excluding periods) with an empty string
        #transcribed_text = re.sub(pattern, ' ', transcribed_text)
        #file.write("({},{})\n".format(segment.start,segment.end))
        # Iterate through the WAV files in the directory

        modified_text = replace_digits_with_words(transcribed_text)

        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
        """
        for filename in os.listdir(wav_directory):
            if filename.endswith(".wav"):
                wav_file_path = os.path.join(wav_directory, filename)
                # Append the data to the list
        """
        data.append(["clips/"+output_file_path[8:],len(segment_audio.export(format="wav").read()),modified_text])
        i+=1
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)  # Write the header
            writer.writerows(data)  # Write the data rows
    print(f'CSV file "{csv_file}" has been created.')
