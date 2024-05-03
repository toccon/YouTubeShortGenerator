from moviepy.editor import *
from utils import choose_random_video, generate_random_name
import numpy as np
import cv2

# slow clip down by a factor specified by factor 
def slowClip(videoFileClip, factor):
    slowed_clip = videoFileClip.speedx(factor)
    return slowed_clip

# takes a clip and returns the clip played twice in a row
def doubleClip(videoFileClip):
    return concatenate_videoclips([videoFileClip, videoFileClip])

# takes a clip and resizes it to have width and height 
# standard for youtube short is 1080 width 1920 height 
def resizeClip(videoFileClip, width, height):
    newclip = videoFileClip.resize((width, height))
    return newclip

# takes clip and 2 points (x1, y1) and (x2, y2) 
# returns a clip cropped from point (x1,y1) to (x2,y2) 
def cropClip(videoFileClip, x1, y1, x2, y2):
    newClip = videoFileClip.crop(x1, y1, x2, y2)
    return newClip

# Takes in moviepy.editor.VideoFileClip and outputName
# exports videoFileClip as a .mp4 with the name outputName.mp4 to the directory video-editor-output
def outputClip(videoFileClip, outputName):
    videoFileClip.write_videofile(f"video-editor-output/{outputName}.mp4")

def make_green_transparent(image):
    # Define the green color range (adjust as needed)
    lower_green = np.array([0, 100, 0])
    upper_green = np.array([80, 255, 80])

    # Create a binary mask for green pixels
    green_mask = cv2.inRange(image[:, :, :3], lower_green, upper_green)

    # Create an alpha channel (transparency channel)
    alpha_channel = np.ones_like(image[:, :, 0]) * 255

    # Set the alpha channel to 0 for green pixels
    alpha_channel[green_mask != 0] = 0

    # Add the alpha channel to the image
    image = cv2.merge((image[:, :, :3], alpha_channel[:, :, np.newaxis]))


    return image

def generate_looping_background_video(totalVideoLength, averageVideoLength, videoDirectory):
    print(f"Total video length is {totalVideoLength}")
    remainingDuration = totalVideoLength
    currentVideoList = []
    videoNames = []

    # split first clip into 2 parts, 1 for beginning of video and 1 for end 
    firstClipName = choose_random_video(f"{videoDirectory}")
    videoNames.append(firstClipName)
    firstClip = VideoFileClip(f"{videoDirectory}/{firstClipName}")
    width, height = firstClip.size
    firstClip = cropClip(firstClip, width/2-540, 0, width/2+540, height)
    firstClip = resizeClip(firstClip, 1080, 1920)
    firstClip1 = firstClip.subclip(firstClip.duration/2, firstClip.duration)
    print(f"firstClip1 duration is {firstClip1.duration}")
    firstClip2 = firstClip.subclip(0, firstClip.duration/2)
    print(f"firstClip2 duration is {firstClip2.duration}")
    
    currentVideoList.append(firstClip1)
    remainingDuration -= firstClip1.duration
    print(f"Adding first clip {firstClipName}, remaining duration is {remainingDuration}")

    # add filler clips in between 
    while remainingDuration > firstClip2.duration + averageVideoLength: 
        videoName = choose_random_video(f"{videoDirectory}")
        currentVideo = VideoFileClip(f"{videoDirectory}/{videoName}")
        if videoNames.__contains__(videoName) or currentVideo.duration > remainingDuration:
            continue
        videoNames.append(videoName)
        
        currentVideo = VideoFileClip(f"{videoDirectory}/{videoName}")
        width, height = currentVideo.size
        currentVideo = cropClip(currentVideo, width/2-540, 0, width/2+540, height)
        currentVideo = resizeClip(currentVideo, 1080, 1920)
        
        currentVideoList.append(currentVideo)
        remainingDuration -= currentVideo.duration
        print(f"Adding clip {videoName} of length {currentVideo.duration}, remaining duration is {remainingDuration}")

    # at this point remainingDuration is less than second half of first clip + coefficient 
    if remainingDuration > firstClip2.duration:
        videoName = choose_random_video(f"{videoDirectory}")
        while videoNames.__contains__(videoName):
            videoName = choose_random_video(f"{videoDirectory}")

        secondLastClip = VideoFileClip(f"{videoDirectory}/{videoName}")
        width, height = secondLastClip.size
        secondLastClip = cropClip(secondLastClip, width/2-540, 0, width/2+540, height)
        secondLastClip = resizeClip(secondLastClip, 1080, 1920)
        secondLastClip = secondLastClip.subclip(0, remainingDuration/2)
        currentVideoList.append(secondLastClip)
        remainingDuration -= secondLastClip.duration
        print(f"Adding second last clip {videoName} of length {secondLastClip.duration}, remaining duration is {remainingDuration}")

        firstClip2 = firstClip2.subclip(0, remainingDuration)
        currentVideoList.append(firstClip2)
        print(f"Adding last clip of length {firstClip2.duration}")
    else:
        firstClip2 = firstClip2.subclip(0, remainingDuration)
        currentVideoList.append(firstClip2)
        print(f"Adding last clip of length {firstClip2.duration}")


    finalVideo = concatenate_videoclips(currentVideoList)
    random_video_name = generate_random_name()
    finalVideo.write_videofile(f"video-editor-output/{random_video_name}.mp4")
    finalVideo.close()
    return random_video_name

def main():

    videoNames = []
    while len(videoNames) < 11:
        videoName = choose_random_video(f"background-videos/iwotd/uncut")
        if videoNames.__contains__(videoName):
            continue
        currentVideo = VideoFileClip(f"background-videos/iwotd/uncut/{videoName}")
        videoNames.append(videoName)
        currentVideoTenSeconds = currentVideo.subclip(0,10)
        currentVideoTenSeconds.write_videofile(f"background-videos/iwotd/10seconds/{videoName}.mp4")
        currentVideo.close()
        currentVideoTenSeconds.close()



    # generate_looping_background_video(24, 10, "background-videos/italian/10seconds")



    # video_name = input("Enter the video file name from directory background-videos-uncut that you would like to edit (without .mp4 extension): ")
    # output_name = input("Enter the file name of the video to be output after edit in directory video-editor-output (without .mp4 extension): ")
    # videoFileClip = VideoFileClip(f"background-videos-uncut/{video_name}.mp4")
    # ########### EDIT CODE HERE 
    # cropped = cropClip(videoFileClip, width/2-540, 0, width/2+540, height)
    # result = resizeClip(cropped, 1080, 1920)
    # outputClip(result, output_name)
    # ########################################
    # cropped.close()
    # result.close()
    # videoFileClip.close()

if __name__ == "__main__":
    main()