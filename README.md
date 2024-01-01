# *VoiceDatasetAz*
## CommonVoiceDataset for deepspeech
- "The dataset for converting prepared text to voice has been created using the Whisper model (by OpenAI)."
- In a sequential dataset consisting of 'path', 'filesize', and 'transcript' columns, the entries describe the location of the audio file, the volume of the voice, and the transcribed text, respectively.
- <p <span style='color:blue'> download clips file https://huggingface.co/datasets/RashadGarazadeh/CommonVoiceAz/blob/main/clips.zip</span> </p>
##### <span style="color:gray">python3.8.8(tested)</span>
- "First, we need to download some libraries and package"
-  ####  <code><span style="color:red">sudo apt install ffmpeg</span></code>
-  ####  <code><span style="color:green">pip install pydub</span></code>
-  #### <code><span style="color:green">pip install faster_whisper</span></code>
<p> Splitting the audio files into segments and placing them into folders using the ffmpeg library because of the large size of the audio files, I've prepared a dataset using the faster_whisper library.</p>
<p>You can use Python scripts in the helper folder to assist in preparing the dataset.</p>



 - By calling the datacreate.py file in the helper directory, you can prepare the train, test, and dev.csv files. Note that you should make changes to the folder names in the file. Also, when translating text within the code, it cleans the text before recording it into the CSV files. Define the values in the code as follows
   
<h4 style="color: red"><code>  python datacreate.py  </code></h4>

<p>"First, by placing a specific portion of audio files into the audio folder, I ensure their availability for the creation of the train.csv. Note that train and dev.csv files should differ in volume; the train.csv file should be significantly larger than dev.csv. Assuming that you have prepared the train.csv file and are moving on to the next, dev.csv, replace the audio files obtained for dev.csv in the audio folder (not in addition to but replacing, ensuring that train, dev, and test files have distinct text and audio). Also, within the datacreate.py file, increment the value of i, representing the number of clips in the clips folder, by one unit. i=22400"</p>
