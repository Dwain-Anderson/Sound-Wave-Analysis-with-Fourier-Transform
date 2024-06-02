import os
import glob
from backend.audio_processing import *
from backend.file_handling import *

current_dir = os.path.dirname(__file__)
test_audio_dir = os.path.join(current_dir, 'test_audios')
test_files = glob.glob(os.path.join(test_audio_dir, '*.wav'))
output_plots_dir = os.path.join(current_dir, 'output_plots')
os.makedirs(output_plots_dir, exist_ok=True)
output_audios_dir = os.path.join(current_dir, 'output_audios')
os.makedirs(output_audios_dir, exist_ok=True)


if __name__ == "__main__":
    for test_file in test_files:
        print(f"Processing {test_file}...")
        plots = process_audio(test_file, filter_type='band-pass', cutoff_frequency=500)
        base_name = os.path.splitext(os.path.basename(test_file))[0]
        with open(os.path.join(output_plots_dir, f'{base_name}_original_audio.png'), 'wb') as f:
            f.write(plots['original_audio_plot'].getbuffer())
        with open(os.path.join(output_plots_dir, f'{base_name}_original_fft.png'), 'wb') as f:
            f.write(plots['original_fft_plot'].getbuffer())
        with open(os.path.join(output_plots_dir, f'{base_name}_filtered_fft.png'), 'wb') as f:
            f.write(plots['filtered_fft_plot'].getbuffer())
        with open(os.path.join(output_plots_dir, f'{base_name}_processed_audio.png'), 'wb') as f:
            f.write(plots['processed_audio_plot'].getbuffer())
        processed_audio_path = os.path.join(output_audios_dir, f'{base_name}_processed.wav')
        save_audio(plots['processed_audio_data'], processed_audio_path)