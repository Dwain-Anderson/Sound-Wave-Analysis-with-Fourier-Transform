import os
from scipy.io import wavfile
import soundfile as sf

def save_file(file, folder):
    filepath = os.path.join(folder, file.filename)
    file.save(filepath)
    return filepath

def save_audio(data, filepath):
    sf.write(filepath, data, samplerate=44100)  # Assuming a sample rate of 44100 Hz, change if necessary
    return filepath

def get_plot_path(filename):
    return os.path.join('plots', filename)

def get_processed_audio_path(filename):
    return os.path.join('processed_audio', filename)

def garbage_collector(threshold):
    plots_folder = 'output_plots'
    uploads_folder = 'uploads'
    processed_audio_folder = 'processed_audio'

    # Check plots folder
    plots_files = os.listdir(plots_folder)
    if len(plots_files) > threshold:
        for file in plots_files:
            os.remove(os.path.join(plots_folder, file))

    # Check uploads folder
    uploads_files = os.listdir(uploads_folder)
    if len(uploads_files) > threshold:
        for file in uploads_files:
            os.remove(os.path.join(uploads_folder, file))

    # Check processed_audio folder
    processed_audio_files = os.listdir(processed_audio_folder)
    if len(processed_audio_files) > threshold:
        for file in processed_audio_files:
            os.remove(os.path.join(processed_audio_folder, file))


