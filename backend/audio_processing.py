import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import os

PLOT_FOLDER = 'plots'

def process_audio(filepath):
    # Read audio file
    samplerate, data = wavfile.read(filepath)
    
    # Perform Fourier Transform
    data_fft = fft(data)
    
    # Example: Apply a simple low-pass filter
    cutoff = 1000  # Frequency in Hz
    data_fft[cutoff:] = 0
    
    # Perform Inverse Fourier Transform
    data_filtered = ifft(data_fft).real.astype(data.dtype)
    
    # Save processed audio file
    output_filepath = filepath.replace('.wav', '_processed.wav')
    wavfile.write(output_filepath, samplerate, data_filtered)
    
    # Generate and save the plot
    plot_filepath = generate_plot(data, data_fft, filepath)
    
    return plot_filepath

def generate_plot(data, data_fft, filepath):
    fig, axs = plt.subplots(2, 1, figsize=(12, 6))

    # Time domain plot
    axs[0].plot(data)
    axs[0].set_title('Time Domain Signal')
    axs[0].set_xlabel('Sample')
    axs[0].set_ylabel('Amplitude')
    
    # Frequency domain plot
    freqs = np.fft.fftfreq(len(data_fft))
    axs[1].plot(freqs, np.abs(data_fft))
    axs[1].set_title('Frequency Domain Signal')
    axs[1].set_xlabel('Frequency')
    axs[1].set_ylabel('Magnitude')
    
    # Save the plot
    plot_filename = os.path.basename(filepath).replace('.wav', '.png')
    plot_filepath = os.path.join(PLOT_FOLDER, plot_filename)
    plt.savefig(plot_filepath)
    plt.close(fig)
    
    return plot_filename
