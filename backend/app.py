from flask import Flask, request, render_template, jsonify
from audio_processing import process_audio
from file_handling import *

app = Flask(__name__)

# Define the paths for saving plots and audios
plots_dir = 'frontend/public/plots'
audios_dir = 'frontend/public/audios'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'audio-file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['audio-file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filepath = save_file(file, 'uploads')
        filter_type = request.form.get('filter-type')
        cutoff_frequency = request.form.get('cutoff-frequency', type=float)
        lowcut = request.form.get('lowcut', type=float)
        highcut = request.form.get('highcut', type=float)

        plots = process_audio(filepath, filter_type, cutoff_frequency, lowcut, highcut)

        base_name = os.path.splitext(os.path.basename(file.filename))[0]
        
        # Save the processed audio
        processed_audio_path = os.path.join('processed_audio', f'{base_name}_processed.wav')
        save_audio(plots['processed_audio'], processed_audio_path)

        #Check if the repo is getting too congested
        garbage_collector(192)

        # Return JSON with URLs for processed audio and plots
        return jsonify({
            'processed_audio': get_processed_audio_path(processed_audio_path),
            'plots': {
                'original_audio': '/audio/' + os.path.basename(filepath),
                'processed_audio': '/audio/' + os.path.basename(processed_audio_path),
                'original_audio_plot': '/plot/' + os.path.basename(plots['original_audio_plot']),
                'original_fft_plot': '/plot/' + os.path.basename(plots['original_fft_plot']),
                'filtered_fft_plot': '/plot/' + os.path.basename(plots['filtered_fft_plot']),
                'processed_audio_plot': '/plot/' + os.path.basename(plots['processed_audio_plot'])
            }
        })

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
