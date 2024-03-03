import moviepy.editor as mp
import os
import sys
from scipy.io import wavfile
import noisereduce as nr
import numpy as np

def removeNoise(video_file):
    # get video file
    clip = mp.VideoFileClip(video_file)
    
    #save audio from that video file
    clip.audio.write_audiofile('temp.wav')

    # load audio data
    rate, data = wavfile.read("temp.wav")

    # perform noise reduction
    orig_shape = data.shape
    data = np.reshape(data, (2, -1)) 
    reduced_noise = nr.reduce_noise(
    y=data,
    sr=rate
    )

    # write deniosed audio to temp file
    wavfile.write("temp_denoised.wav", rate, reduced_noise.reshape(orig_shape))

    # get audio from saved file
    audio = mp.AudioFileClip('temp_denoised.wav')

    # merge denoised audio and video
    final_video = clip.set_audio(audio)

    # get file name from filename and its extension
    filename, ext = os.path.splitext(video_file)

    # write the video file
    final_video.write_videofile(f"{filename} denoised.mp4")

    # remove recently generated unnecessary files
    os.remove('temp.wav')
    os.remove('temp_denoised.wav')

if __name__ == "__main__":
    vf = sys.argv[1]
    removeNoise(vf)
