import os
import random
import string

def generate_random_name(length=10):
    """Generate a random video name of characters and numbers."""
    characters = string.ascii_letters + string.digits  # A combination of letters and numbers
    random_name = ''.join(random.choice(characters) for _ in range(length))
    return random_name

def choose_random_video(directory):
    video_files = [f for f in os.listdir(directory) if f.endswith('.mp4') or f.endswith('.mp3')]
    
    if not video_files:
        print("No .mp4 files found in the directory.")
        return None
    
    chosen_video = random.choice(video_files)
    return chosen_video