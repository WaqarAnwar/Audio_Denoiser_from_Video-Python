# Audio Denoiser from Video

Hello! This is a basic noise removing script using Python. 

It uses noisereduce library to reduce the noise from the audio and moviepy library to merge audio and video.

Advantages: Normally it takes 4 to 5 hours to remove noise from a video as first you have to split audio and video, 
then remove noise from the audio then merge audio and video back. But this method is faster and it lowers the time from 4-8 hours to 1-2 hours per video
(assuming the video is more than an hour long). And it does all of it in one go. Just input a video and it will output a denoised video.
The time to generate the video is much shorter as compared to some conventional video editors these days.

Disadvantages: It might not remove all the noise as it generally assumes noise levels and reduces the noise. Also sometimes the audio and video go out of sync after 45 minutes if the video
is more than 45 minutes long. This is due to moviepy library not merging the audio and video correctly.

Here is the Noisy Audio Plot:
![alt text](https://github.com/WaqarAnwar/Audio_Noise_Remover_from_Video-Python/blob/main/NoisyAudioPlot.PNG?raw=true)

And here is the Denoised Audio Plot:
![alt text](https://github.com/WaqarAnwar/Audio_Noise_Remover_from_Video-Python/blob/main/DenoisedAudioPlot.PNG?raw=true)

## Usage

Make virtual environment and then activate that virtual environment.

Then run:
```bash
  pip install -r requirements.txt
```
Then copy your video to the current directory where these files are located.

Then to remove noise from a video "video.mp4", run:
```bash
  python noise_remover.py "video.mp4"
```
And it will successfully remove noise from the provided video and generate a new denoised video.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
