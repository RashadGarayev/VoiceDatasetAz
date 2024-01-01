# *VoiceDatasetAz*
## CommonVoiceDataset for deepspeech
- "The dataset for converting prepared text to voice has been created using the Whisper model (by OpenAI)."
- In a sequential dataset consisting of 'path', 'filesize', and 'transcript' columns, the entries describe the location of the audio file, the volume of the voice, and the transcribed text, respectively.
- <p <span style='color:blue'> download clips file https://huggingface.co/datasets/RashadGarazadeh/CommonVoiceAz/blob/main/clips.zip</span> </p>
##### <span style="color:gray">python3.8.8(tested)</span>
- "First, we need to download some libraries and package"
- ###  <code><span style="color:red">sudo apt install ffmpeg</span></code>
- ### 2. <code><span style="color:green">pip install pydub</span></code>
- ### 3. <code><span style="color:green">pip install faster_whisper</span></code>
<p> Splitting the audio files into segments and placing them into folders using the ffmpeg library because of the large size of the audio files, I've prepared a dataset using the faster_whisper library.</p>
