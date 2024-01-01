import subprocess
import os

def export_and_split_audio(input_file, output_folder, num_parts):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Export audio from MP4
    audio_output_file = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(input_file))[0]}_audio.mp3")
    subprocess.run(['ffmpeg', '-i', input_file, '-vn', '-acodec', 'libmp3lame', audio_output_file])

    # Split the audio into parts
    part_duration = get_audio_duration(audio_output_file) / num_parts
    for i in range(num_parts):
        part_output_file = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(input_file))[0]}_part_{i + 1}.mp3")
        start_time = i * part_duration
        subprocess.run(['ffmpeg', '-i', audio_output_file, '-acodec', 'copy', '-ss', str(start_time), '-t', str(part_duration), part_output_file])

def get_audio_duration(audio_file):
    result = subprocess.run(['ffprobe', '-i', audio_file, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=p=0'], stdout=subprocess.PIPE, text=True)
    return float(result.stdout.strip())

if __name__ == "__main__":
    input_files = [r"/home/user/Downloads/mp/1.mp4", r"/home/user/Downloads/mp/2.mp4",r"/home/user/Downloads/mp/3.mp4"]
    output_folder = r"/home/user/Downloads/output"
    num_parts = 3

    for input_file in input_files:
        export_and_split_audio(input_file, output_folder, num_parts)

