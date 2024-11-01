from atproto import Client
from pathlib import Path
import time
import os, os.path
import pickle
import ast
import requests

client = Client()
client.login('everyonepieceframe.bsky.social', 'Store-Cast-0952')

# Hardcoded defaults
frameNum = 0
currentFrame = 0
file_name = 'values.txt'

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

def save_values(input_value_1, input_value_2, filename):
    with open(file_name, 'w') as f:
        f.write(str(f"{input_value_1},{input_value_2}"))

def load_value(filename):
    with open(filename, 'r') as f:
        read = []
        read = f.read().split(",")
        return read


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

    values = load_value(file_name)

    while (True):
        for i in range(int(values[0]), 1123):

            values = load_value(file_name)

            folder_dir = f'One Piece Frames/E{i}' # Change so that the season folder is removed, unnecessary and overcomplicated
            frameNum = countEps(folder_dir)
            for j in range(int(values[1]), frameNum+1):
                try:
                    with open(f"One Piece Frames/E{i}/OnePieceFrame ({j}).jpeg", 'rb') as f:
                        img_data = f.read()
                        client.send_image(text=f'One Piece Episode {i} Frame ({j}/{frameNum})', image=img_data, image_alt=f'One Piece Episode {i} Frame ({j}/{frameNum})')
                        print(f"Frame {j} out of {frameNum} has been posted!")
                        save_values(i, j+1, file_name)
                        time.sleep(300) # Change back to 300 after testing
                    
                except:
                    print("Error has occurred")
                    time.sleep(60)
                
                
            save_values(i, "1", file_name)

main()