import os
from pydub import AudioSegment
from gtts import gTTS
from utils import generate_random_name
from moviepy.editor import AudioFileClip, concatenate_audioclips

ENGLISH = "en"
ITALIAN = "it"
PAUSE = "pause"

def text_to_speech(language, text, fileName):
    if(language == "english"):
        return text_to_speech_english(text, fileName)
    elif(language == "portugese"):
        return text_to_speech_portugese(text, fileName)
    elif(language == "italian"):
        return text_to_speech_italian(text, fileName)
    elif(language == "french"):
        return text_to_speech_french(text, fileName)
    elif(language == "spanish"):
        return text_to_speech_spanish(text, fileName)

def text_to_speech_english(text, fileName, language='en', tld='us'):
    """Converts text to speech using Google Text-to-Speech (gTTS), saves resultig .mp3 in temp/fileName and returns a moviePy.AudioFileClip.

    Args:
        text (str): string to be read
        fileName (str): output file name temp/fileName
        language (str, optional): Language of translation. Defaults to 'en'.
        tld (str, optional): top-level domain (accent). From https://gtts.readthedocs.io/en/latest/module.html#module-gtts.tts.

    Returns:
        moviePy.AudioFileClip: AudioFileClip representing the tts.
    """
    tts = gTTS(text=text, lang=language, tld=tld, slow=True)
    tts.save(f"temp/{fileName}.mp3")
    audio_clip = AudioFileClip(f"temp/{fileName}.mp3")
    return audio_clip

def text_to_speech_italian(text, fileName, language='it'):
    """Converts text to Italian speech using Google Text-to-Speech (gTTS), saves resultig .mp3 in temp/fileName and returns a moviePy.AudioFileClip.

    Args:
        text (str): string to be read
        fileName (str): output file name temp/fileName
        language (str, optional): Defaults to 'it'.

    Returns:
        moviePy.AudioFileClip: AudioFileClip representing the tts.
    """
    tts = gTTS(text=text, lang=language, slow=True)
    tts.save(f"temp/{fileName}.mp3")
    audio_clip = AudioFileClip(f"temp/{fileName}.mp3")
    return audio_clip

def text_to_speech_portugese(text, fileName, language="pt"):
    """Converts text to Portugese speech using Google Text-to-Speech (gTTS), saves resultig .mp3 in temp/fileName and returns a moviePy.AudioFileClip.

    Args:
        text (str): string to be read
        fileName (str): output file name temp/fileName
        language (str, optional): Defaults to 'pt'.

    Returns:
        moviePy.AudioFileClip: AudioFileClip representing the tts.
    """
    tts = gTTS(text=text, lang=language, tld="pt", slow=True)
    tts.save(f"temp/{fileName}.mp3")
    audio_clip = AudioFileClip(f"temp/{fileName}.mp3")
    return audio_clip

def text_to_speech_french(text, fileName, language="fr"):
    """Converts text to French speech using Google Text-to-Speech (gTTS), saves resultig .mp3 in temp/fileName and returns a moviePy.AudioFileClip.

    Args:
        text (str): string to be read
        fileName (str): output file name temp/fileName
        language (str, optional): Defaults to 'pt'.

    Returns:
        moviePy.AudioFileClip: AudioFileClip representing the tts.
    """
    tts = gTTS(text=text, lang=language, tld="fr", slow=True)
    tts.save(f"temp/{fileName}.mp3")
    audio_clip = AudioFileClip(f"temp/{fileName}.mp3")
    return audio_clip

def text_to_speech_spanish(text, fileName, language="es"):
    """Converts text to Spanish speech using Google Text-to-Speech (gTTS), saves resultig .mp3 in temp/fileName and returns a moviePy.AudioFileClip.

    Args:
        text (str): string to be read
        fileName (str): output file name temp/fileName
        language (str, optional): Defaults to 'pt'.

    Returns:
        moviePy.AudioFileClip: AudioFileClip representing the tts.
    """
    tts = gTTS(text=text, lang=language, tld="es", slow=True)
    tts.save(f"temp/{fileName}.mp3")
    audio_clip = AudioFileClip(f"temp/{fileName}.mp3")
    return audio_clip

def silent_audio(duration, fileName):
    """_summary_

    Args:
        duration (_type_): _description_
        fileName (_type_): _description_

    Returns:
        _type_: _description_
    """
    silence = AudioSegment.silent(duration=duration * 1000)  
    silence.export(f"temp/{fileName}.mp3")
    audio_clip = AudioFileClip(f"temp/{fileName}.mp3")
    return audio_clip