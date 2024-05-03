from moviepy.editor import AudioFileClip, ImageClip
from utils import choose_random_video

def getBackgroundMusic(language):
    # Add background music
    if(language == "portugese"):
        backgroundMusicName = choose_random_video(f"background-music/portugese")
        print(f"Audio being used is {backgroundMusicName}")
        backgroundMusic = AudioFileClip(f"background-music/portugese/{backgroundMusicName}") 
    elif(language == "italian"):
        backgroundMusicName = choose_random_video(f"background-music/italian")
        print(f"Audio being used is {backgroundMusicName}")
        backgroundMusic = AudioFileClip(f"background-music/italian/{backgroundMusicName}")
    elif(language == "french"):
        backgroundMusicName = choose_random_video(f"background-music/french")
        print(f"Audio being used is {backgroundMusicName}")
        backgroundMusic = AudioFileClip(f"background-music/french/{backgroundMusicName}")
    elif(language == "spanish"):
        backgroundMusicName = choose_random_video(f"background-music/spanish")
        print(f"Audio being used is {backgroundMusicName}")
        backgroundMusic = AudioFileClip(f"background-music/spanish/{backgroundMusicName}")
    
    return backgroundMusic

def getLogo(language):
    if(language == "portugese"):
        logoClip = ImageClip("logos/pwotd/orange-circle-logo.png")
    elif(language == "italian"):
        logoClip = ImageClip("logos/iwotd/circle_logo_blue.png")
    elif(language == "french"):
        logoClip = ImageClip("logos/fwotd/circle-logo.png")
    elif(language == "spanish"):
        logoClip = ImageClip("logos/swotd/circle-logo.png")

    return logoClip

def getSubscribeAudio(language):
    if(language == "italian"):
        subscribe = "Per favore, iscriviti."
    elif(language == "portugese"):
        subscribe = "Por favor, subscreva."
    elif(language == "french"):
        subscribe = "S'il vous plait, abonnez-vous."
    elif(language == "spanish"):
        subscribe = "Por favor, suscríbete."

    return subscribe

def getDirectories(language):
    if language == "italian":
        BACKGROUND_VIDEO_DIRECTORY = "background-videos/iwotd/10seconds"
        STAGING_DIRECTORY = "staging/iwotd"
    elif language == "portugese":
        BACKGROUND_VIDEO_DIRECTORY = "background-videos/pwotd/10seconds"
        STAGING_DIRECTORY = "staging/pwotd"
    elif language == "french":
        BACKGROUND_VIDEO_DIRECTORY = "background-videos/fwotd/10seconds"
        STAGING_DIRECTORY = "staging/fwotd"
    elif language == "spanish":
        BACKGROUND_VIDEO_DIRECTORY = "background-videos/swotd/10seconds"
        STAGING_DIRECTORY = "staging/swotd"

    return BACKGROUND_VIDEO_DIRECTORY, STAGING_DIRECTORY