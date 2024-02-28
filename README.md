Hello! This is a basic noise removing software using Python. 

To use it, make virtual environment and then activate that virtual environment.

Then run:
  pip install -r requirements.txt

Then copy your video to the current directory where these files are located.

Then to remove noise from a video "video.mp4", run:
  python noise_remover.py "video.mp4"

And it will successfully remove noise from the provided video and generate a new denoised video.

Advantages: Normally it takes 4 to 5 hours to remove noise from a video as first you have to split audio and video, 
then remove noise from the audio then merge audio and video back. But this method is faster and it lowers the time from 4-8 hours to 1-2 hours per video
(assuming the video is more than an hour long). And it does all of it in one go. The time to generate the video is much shorter as compared to some conventional video editors these days.

Disadvantages: It might not remove all the noise as it generally assumes noise levels and reduces the noise.
