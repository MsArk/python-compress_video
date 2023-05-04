import os
from dotenv import load_dotenv
load_dotenv()

import moviepy.editor as mp

INPUT_FILE = os.getenv('INPUT_FILE')
OUTPUT_FILE = os.getenv('OUTPUT_FILE')

clip = mp.VideoFileClip(INPUT_FILE)
clip_resized = clip.resize(height = 1080)
clip_resized.write_videofile(OUTPUT_FILE)
