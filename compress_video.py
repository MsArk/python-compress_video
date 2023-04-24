# pip install moviepy
import moviepy.editor as mp

clip = mp.VideoFileClip("VIDEO_INPUT.MP4")
clip_resized = clip.resize(height = 1080)
clip_resized.write_videofile("VIDEO_INPUT_Resized.mp4")
