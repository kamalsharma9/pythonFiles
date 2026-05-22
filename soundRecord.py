import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io.wavfile import write
import sounddevice as sd

# Recording parameters
duration = 4          # seconds
fs = 44100            # sampling frequency

print("Recording for 4 seconds...")

# Record audio
audio = sd.rec(int(duration * fs),
               samplerate=fs,
               channels=1,
               dtype='float64')

# Wait until recording finishes
sd.wait()

print("Recording finished.")

# Convert to 1D array
audio = audio.flatten()

# -------------------------------
# SAVE AUDIO TO WAV FILE
# -------------------------------

# Convert float audio (-1 to 1)
# into 16-bit integer format
audio_int16 = np.int16(audio * 32767)

# Save file
write("recorded_audio.wav", fs, audio_int16)

print("Audio saved as recorded_audio.wav")

# -------------------------------
# FFT COMPUTATION
# -------------------------------

# Number of samples
N = len(audio)

# Compute FFT
yf = fft(audio)

# Frequency axis
xf = fftfreq(N, 1 / fs)

# Positive frequencies only
positive_freqs = xf[:N // 2]

# Magnitude spectrum
magnitude = 2.0 / N * np.abs(yf[:N // 2])

# -------------------------------
# PLOT FFT
# -------------------------------

plt.figure(figsize=(10, 5))
plt.plot(positive_freq,magnitude)

plt.title("FFT of Recorded Audio")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.grid(True)
plt.show()
