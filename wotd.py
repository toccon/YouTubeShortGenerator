from moviepy.editor import CompositeAudioClip, VideoFileClip, concatenate_audioclips
from gTTSutils import text_to_speech_english, silent_audio, text_to_speech
from moviePyUtils import createTextClip
from wotdUtils import getLogo, getBackgroundMusic
from videoEditor import resizeClip

def createWOTDScene(language, wotd, pronounced, wordType, translation, exampleSentence, exampleSentenceTranslation, subscribe):
    # Audio
    audioClips = []

    # 5 second pause at beginning of clip
    audioClips.append(silent_audio(5, "silence"))
    totalClipDuration = 5 

    # Audio for WOTD
    wotdAudioClip = text_to_speech(language, wotd, "wotdAudioClip")
    audioClips.append(wotdAudioClip)
    totalClipDuration += wotdAudioClip.duration

    # 2 second pause between WOTD and definition
    audioClips.append(silent_audio(2, "silence"))
    totalClipDuration += 2

    # Audio for translation
    translationAudioClip = text_to_speech_english(translation, "definitionAudioClip")
    audioClips.append(translationAudioClip)
    totalClipDuration += translationAudioClip.duration

    # 2 second pause after translation
    audioClips.append(silent_audio(2, "silence"))
    totalClipDuration += 2
    timeWhenExampleSentenceAppears = totalClipDuration

    # Audio for example sentence
    exampleSentenceAudio = text_to_speech(language, exampleSentence, "exampleSentenceAudioClip")
    audioClips.append(exampleSentenceAudio)
    totalClipDuration += exampleSentenceAudio.duration
    exampleSentenceWords = exampleSentence.split()
    print(f"Audio for example sentence {exampleSentence} is {exampleSentenceAudio.duration} long for {len(exampleSentenceWords)} words")

    # 2 second pause after example sentence
    audioClips.append(silent_audio(2, "silence"))
    totalClipDuration += 2
    timeWhenExampleSentenceTranslationAppears = totalClipDuration
    
    # Audio for example sentence translation
    exampleSentenceTranslationAudio = text_to_speech_english(exampleSentenceTranslation, "exampleSentenceTranslationAudioClip")
    audioClips.append(exampleSentenceTranslationAudio)
    totalClipDuration += exampleSentenceTranslationAudio.duration

    # 4 second pause after example sentence translation
    audioClips.append(silent_audio(5, "silence"))
    totalClipDuration += 4

    # Audio for please like and subscribe
    subscribeAudio = text_to_speech(language, subscribe, "subscribeAudio")
    audioClips.append(subscribeAudio)
    totalClipDuration += subscribeAudio.duration

    # 1 second pause after subscribe 
    audioClips.append(silent_audio(2, "silence"))
    totalClipDuration += 2

    # Add background music
    backgroundMusic = getBackgroundMusic(language)
    backgroundMusic = backgroundMusic.set_start(0).set_duration(totalClipDuration)
    backgroundMusic = backgroundMusic.volumex(0.1)

    # Final Audio
    result = concatenate_audioclips(audioClips)
    result = result.set_duration(totalClipDuration)
    resultWithBackgroundMusic = CompositeAudioClip([backgroundMusic, result])
    resultWithBackgroundMusic = resultWithBackgroundMusic.set_duration(totalClipDuration)
    resultWithBackgroundMusic.write_audiofile(f"gtts-output/finalIntroAudio.mp3", fps=16000)
    
    textClips = []

    # ImageClip for logo 
    logoClip = getLogo(language)
    logoClip = logoClip.set_position((419, 100)).set_start(2)
    logoClip = logoClip.set_duration(totalClipDuration - logoClip.start).crossfadein(2).crossfadeout(1)
    textClips.append(logoClip)

    # TextClip for phonetic meaning (pronounciation)
    pronounciationClip = createTextClip(text=pronounced, font="Arial-Italic", fontsize=70, color='white', border_color='black', border_width=2, start=5)
    pronounciationClip = pronounciationClip.set_position((600-pronounciationClip.size[0], 650))
    pronounciationClip = pronounciationClip.set_duration(totalClipDuration - pronounciationClip.start - 4).crossfadein(2).crossfadeout(1)
    textClips.append(pronounciationClip)

    # TextClip for WOTD
    wotdClip = createTextClip(text=wotd, font="Arial-Bold", fontsize=140, color="white", border_color="black", border_width=3, start=4)
    wotdClip = wotdClip.set_position(((1080-wotdClip.size[0])/2, 700))
    wotdClip = wotdClip.set_duration(totalClipDuration - wotdClip.start - 4).crossfadein(2).crossfadeout(1)
    textClips.append(wotdClip)
    
    # TextClip for word type (example greeting, verb, adjective, etc.)
    wordTypeClip = createTextClip(text=wordType, font="Arial-Italic", fontsize=50, color="white", border_color='black', border_width=2, start=5)
    wordTypeClip = wordTypeClip.set_position((640, 850))
    wordTypeClip = wordTypeClip.set_duration(totalClipDuration - wordTypeClip.start - 4).crossfadein(2).crossfadeout(1)
    textClips.append(wordTypeClip)

    # TextClip for english translation
    translationClip = createTextClip(text=translation, font="Arial-Bold", fontsize=100, color="white", border_color='black', border_width=3, start=8)
    translationClip = translationClip.set_position(((1080-translationClip.size[0])/2, 1000))
    translationClip = translationClip.set_duration(totalClipDuration - translationClip.start - 4).crossfadein(1).crossfadeout(1)
    textClips.append(translationClip)

    # TextClip for example sentence
    exampleSentenceClip = createTextClip(text=exampleSentence, font="Arial", fontsize=80, color="white", border_color='black', border_width=3, method="caption", size=(900,1920))
    exampleSentenceClip = exampleSentenceClip.set_position(((1080-exampleSentenceClip.size[0])/2, 300))
    exampleSentenceClip = exampleSentenceClip.set_start(timeWhenExampleSentenceAppears)
    exampleSentenceClip = exampleSentenceClip.set_duration(totalClipDuration - timeWhenExampleSentenceAppears - 4).crossfadein(1).crossfadeout(1)
    textClips.append(exampleSentenceClip)

    # TextClip for example sentence translation
    exampleSentenceTranslationClip = createTextClip(text=exampleSentenceTranslation, font="Arial-Italic", fontsize=80, color="white", border_color='black', border_width=3, method="caption", size=(900,1920))
    if len(exampleSentenceWords) < 5:
        exampleSentenceTranslationClip = exampleSentenceTranslationClip.set_position(((1080-exampleSentenceTranslationClip.size[0])/2, 450))
    elif len(exampleSentenceWords) >= 5:
        exampleSentenceTranslationClip = exampleSentenceTranslationClip.set_position(((1080-exampleSentenceTranslationClip.size[0])/2, 500))
    exampleSentenceTranslationClip = exampleSentenceTranslationClip.set_start(timeWhenExampleSentenceTranslationAppears)
    exampleSentenceTranslationClip = exampleSentenceTranslationClip.set_duration(totalClipDuration - timeWhenExampleSentenceTranslationAppears - 4).crossfadein(1).crossfadeout(1)
    textClips.append(exampleSentenceTranslationClip)

    # VideoClip for please like an subscribe
    subscribe = VideoFileClip("background-videos/general/1gif.gif", has_mask=True)
    subscribe = resizeClip(subscribe, 960, 540)
    subscribe = subscribe.set_position("center")
    subscribe = subscribe.subclip(1, subscribe.duration-1)
    subscribe = subscribe.set_start(totalClipDuration-4)
    subscribe = subscribe.set_duration(4)
    subscribe = subscribe.crossfadein(1).crossfadeout(1)
    print(f"video size is {subscribe.size} with duration {subscribe.duration}")
    textClips.append(subscribe)

    # Subclip background video to be the correct length 
    print(f"Duration of total video clip: {totalClipDuration}")
    return textClips, totalClipDuration