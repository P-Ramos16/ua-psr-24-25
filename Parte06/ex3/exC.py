import pyaudio
import webrtcvad
import wave

import numpy as np

# Audio configuration
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open stream
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

# Initialize VAD
vad = webrtcvad.Vad()
vad.set_mode(1)  # 0: Aggressive filtering, 3: Less aggressive


def main():
    # Example usage
    frames = record_audio()
    save_audio(frames)
    print("Audio saved as output.wav")


def is_speech(frame, sample_rate):
    return vad.is_speech(frame, sample_rate)

def record_audio():
    frames = []
    recording = False

    print("Listening for speech...")

    while True:
        frame = stream.read(CHUNK)

        if is_speech(frame, RATE):
            if not recording:
                print("Recording started.")
                recording = True
            frames.append(frame)
        else:
            if recording:
                print("Silence detected, stopping recording.")
                break

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    return frames


def save_audio(frames, filename="output.wav"):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()



if __name__ == '__main__':
    main()