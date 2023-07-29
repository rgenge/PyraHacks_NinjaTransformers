import pyaudio
import numpy as np
 
pA = pyaudio.PyAudio()

incomingStream = pA.open(format=pyaudio.paInt16,
                   channels=1,
                   rate=44100,
                   input=True,
                   frames_per_buffer=1024)

outgoingStream = pA.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    output=True,
                    frames_per_buffer=1024)

#Define functions to change volume and pitch:
def volume_amplication(data, scale_factor):
    # Scale the audio data by the given factor
    return (data * scale_factor).astype(np.int16)

def pitch_lowering(data, semitones):
    # Change the pitch of the audio data by the given number of semitones
    data_float = data.astype(np.float32)
    y_pitched = np.interp(np.arange(0, len(data)), np.arange(0, len(data)) * (2 ** (semitones / 12.0)), data_float)
    return y_pitched.astype(np.int16)

volume_scale = 0
#Run the audio processing loop:
def main():
    #Make scale to gather volume input
    volume_scale = int(input("How high would you like to set the volume from 1 (lowest) to 5 (highest)?\n"))
    pitch_semitones = int(input("lower the pitch by entering a number greater than 0 (the higher the number the lower the pitch)!\n"))

    print("enter Ctrl+C to exit.")

    try:
        while True:
            # Read audio data from the input stream
            input_data = np.frombuffer(incomingStream.read(1024), dtype=np.int16)

            # Apply volume and pitch changes
            processed_data = volume_amplication(input_data, volume_scale)
            processed_data = pitch_lowering(processed_data, pitch_semitones)

            # Play the processed audio data
            outgoingStream.write(processed_data.tobytes())

    except KeyboardInterrupt:
        print("\nExiting the program.")
    finally:
        # Close the audio streams
        incomingStream.stop_stream()
        incomingStream.close()
        outgoingStream.stop_stream()
        outgoingStream.close()
        pA.terminate()

if __name__ == "__main__":
    main()