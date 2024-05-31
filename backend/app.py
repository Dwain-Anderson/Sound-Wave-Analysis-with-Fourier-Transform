from flask import Flask, request, jsonify, send_from_directory, send_file
from audio_processing import process_audio, generate_plot
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
PLOT_FOLDER = 'plots'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(PLOT_FOLDER):
    os.makedirs(PLOT_FOLDER)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'audio-file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['audio-file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        plot_filepath = process_audio(filepath)
        return jsonify({'success': 'File processed successfully', 'plot': plot_filepath}), 200

@app.route('/plot/<filename>')
def serve_plot(filename):
    return send_file(os.path.join(PLOT_FOLDER, filename), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
