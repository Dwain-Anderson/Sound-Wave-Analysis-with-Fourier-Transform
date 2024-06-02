import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt
import io

def read_audio_file(filepath):
    sample_rate, data = wavfile.read(filepath)
    return sample_rate, data

def get_channel(data):
    if len(data.shape) > 1:
        return data[:, 0]
    return data

def fast_fourier_transform(data, sample_rate):
    fft_values = np.fft.fft(data)
    fft_frequencies = np.fft.fftfreq(len(data), 1 / sample_rate)
    return fft_values, fft_frequencies

def inverse_fourier_transform(fft_values):
    return np.fft.ifft(fft_values)

def low_band_filter(data, sample_rate, cutoff):
    nyquist = 0.5 * sample_rate
    normal_cutoff = cutoff / nyquist
    b, a = butter(1, normal_cutoff, btype='low', analog=False)
    return filtfilt(b, a, data)

def high_band_filter(data, sample_rate, cutoff):
    nyquist = 0.5 * sample_rate
    normal_cutoff = cutoff / nyquist
    b, a = butter(1, normal_cutoff, btype='high', analog=False)
    return filtfilt(b, a, data)

def band_pass_filter(data, sample_rate, lowcut, highcut):
    nyquist = 0.5 * sample_rate
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(1, [low, high], btype='band')
    return filtfilt(b, a, data)

def plot_audio(data, sample_rate, title='Audio Signal'):
    time = np.arange(len(data)) / sample_rate
    plt.figure(figsize=(10, 4))
    plt.plot(time, data)
    plt.title(title)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return img

def plot_fft(frequencies, fft_values, title='FFT of Audio Signal'):
    plt.figure(figsize=(10, 4))
    plt.plot(frequencies, np.abs(fft_values))
    plt.title(title)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.xlim(0, max(frequencies) / 2)  # Nyquist limit
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return img

def process_audio(filepath, filter_type, cutoff_frequency=None, lowcut=None, highcut=None):
    sample_rate, data = read_audio_file(filepath)
    data = get_channel(data)

    original_audio_plot = plot_audio(data, sample_rate, title='Original Audio Signal')
    fft_values, fft_frequencies = fast_fourier_transform(data, sample_rate)
    original_fft_plot = plot_fft(fft_frequencies, fft_values, title='FFT of Original Audio Signal')

    if filter_type == 'low-pass':
        filtered_data = low_band_filter(data, sample_rate, cutoff_frequency)
    elif filter_type == 'high-pass':
        filtered_data = high_band_filter(data, sample_rate, cutoff_frequency)
    elif filter_type == 'band-pass':
        filtered_data = band_pass_filter(data, sample_rate, lowcut, highcut)
    else:
        raise ValueError("Invalid filter type")

    fft_filtered_values, fft_filtered_frequencies = fast_fourier_transform(filtered_data, sample_rate)
    filtered_fft_plot = plot_fft(fft_filtered_frequencies, fft_filtered_values, title='FFT of Filtered Audio Signal')
    processed_audio_data = np.real(inverse_fourier_transform(fft_filtered_values))

    processed_audio_plot = plot_audio(processed_audio_data, sample_rate, title='Processed Audio Signal')

    return {
        'original_audio_plot': original_audio_plot,
        'original_fft_plot': original_fft_plot,
        'filtered_fft_plot': filtered_fft_plot,
        'processed_audio_data': processed_audio_data,
        'processed_audio_plot': processed_audio_plot
    }
