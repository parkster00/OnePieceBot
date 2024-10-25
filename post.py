from atproto import Client
from pathlib import Path
import time
import os, os.path

client = Client()
client.login('everyonepieceframe.bsky.social', 'Store-Cast-0952')

# Hardcoded defaults
frameNum = 0
currentFrame = 0

def countEps(folder_dir):
    # folder path
    dir_path = folder_dir
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    return count


# def adminMenu():
#     #global folder_dir
#     global episode
#     global currentFrame

#     print("Ahoy! Please enter what season, episode, and what frame we're on:\n")
#     episode = int(input("Episode: "))
#     currentFrame = int(input("Current frame: "))
#     #folder_dir = f'One Piece Frames/E{episode}/'
#     print("Thanks! One moment while I start the bot...")
#     #time.sleep(5)


def main():

    # adminMenu()

    # global episode
    # global currentFrame

    while (True):
        for i in range(2, 1123):
            folder_dir = f'OnePieceBot/One Piece Frames/E{i}' # Change so that the season folder is removed, unnecessary and overcomplicated
            frameNum = countEps(folder_dir)
            for j in range(0, frameNum+1):
                try:
                    with open(f"OnePieceBot/One Piece Frames/E{i}/OnePieceFrame ({j}).jpeg", 'rb') as f:
                        img_data = f.read()
                        client.send_image(text=f'One Piece Episode {i} Frame ({j}/{frameNum})', image=img_data, image_alt=f'One Piece Episode {i} Frame ({j}/{frameNum})')
                        print(f"Frame {j} out of {frameNum} has been posted!")
                        time.sleep(300) # Change back to 900 after testing
                    
                except:
                    print("Error has occurred")
                    time.sleep(60)

main()