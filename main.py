import pandas as pd
from moviepy.editor import VideoFileClip, CompositeVideoClip
from videoEditor import generate_looping_background_video
from wotd import createWOTDScene
from wotdUtils import getSubscribeAudio, getDirectories

SUPPORTED_LANGUAGES = {"italian": "spreadsheets/iwotd/italian-words-and-definitions.xlsx", 
                       "portugese": "spreadsheets/pwotd/portugese-words-and-translations.xlsx",
                       "french": "spreadsheets/fwotd/french-words-and-translations.xlsx",
                       "spanish": "spreadsheets/swotd/spanish-words-and-translations.xlsx"}

def main():
    language = get_language_user_input()
    BACKGROUND_VIDEO_DIRECTORY, STAGING_DIRECTORY = getDirectories(language)
    
    file_path = SUPPORTED_LANGUAGES.get(language)
    print("Reading .xlsx file" + file_path)
    
    df = pd.read_excel(file_path)
    max_rows = get_max_rows_user_input()

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        
        if(index == max_rows):
            break

        wotd = str(row['Word']).strip()
        translation = str(row['Translation']).strip()
        pronunciation = str(row['Pronunciation']).strip()
        word_type = str(row['Word Type']).strip()

        example_sentence1 = str(row['Example Sentence 1']).strip()
        english_translation1 = str(row['English Translation 1']).strip()

        subscribe = getSubscribeAudio(language)

        wotdSceneClips, wotdSceneDuration = createWOTDScene(language, wotd, pronunciation, word_type, translation, example_sentence1, english_translation1, subscribe)

        backgroundVideoName = generate_looping_background_video(wotdSceneDuration, 10, BACKGROUND_VIDEO_DIRECTORY)
        backgroundVideo = VideoFileClip(f"video-editor-output/{backgroundVideoName}.mp4")
        backgroundVideo = backgroundVideo.set_duration(wotdSceneDuration)

        # Add background vid
        wotdSceneClips.insert(0, backgroundVideo)
        introSceneWithBackground = CompositeVideoClip(wotdSceneClips)

        # Output final video
        introSceneWithBackground.write_videofile(f"{STAGING_DIRECTORY}/{wotd}.mp4", audio='gtts-output/finalIntroAudio.mp3')

        # Close clips
        backgroundVideo.close()
        introSceneWithBackground.close()

# Function to get user input for the number of rows
def get_max_rows_user_input():
    while True:
        try:
            num_rows = int(input("Enter the number of rows to generate: "))
            if num_rows > 0:
                return num_rows
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Function to get user input for the language
def get_language_user_input():
    while True:
        try:
            language = input("Enter the language: ")
            if language.lower() in SUPPORTED_LANGUAGES:
                return language.lower()
            else:
                while language.lower() not in SUPPORTED_LANGUAGES:
                    print("Please enter one of the supported languages.")
                    print(SUPPORTED_LANGUAGES)
                    language = input("Enter the language: ")
        except ValueError:
            print("Invalid input. Please enter a supported language.")


# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()