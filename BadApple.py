from colorsys import rgb_to_hls
import numpy as np
from PIL import Image
import time
import sys
from PIL.ImageOps import grayscale
from numpy._core.fromnumeric import resize
from playsound3 import playsound
from threading import Thread
#Value for resizing the img to fit in the terminal
hauteur = 63
largeur = 130

#Path and actual frame,priting into the console
#Use to play soung
def play_sound():
    playsound("BadApple.mp3")

def data_image(path:str):
    """Get image array pixeldata"""
    image = Image.open(path)
    image = grayscale(image)
    #Resize the image
    image = image.resize((largeur,hauteur))
    #Convert the image into a readable array
    return np.array(image)
def play_video():
    frame = 1
    affichage = ""
    while frame < 6572:
        #Path to find the image
        path = f"frames/output_{frame:04}.jpg"
        #Call function data_image to get an array
        data =data_image(path)
        for y in range(hauteur):
            affichage+="\n"
            for x in range(largeur):
                if data[y,x]==0:
                    affichage +="0"
                else:
                    affichage+="1"
        #Next frame
        frame +=1
        #Print into the console (i have look online for alternative to print )
        sys.stdout.write(affichage)
        #Reset the print
        affichage =""
        time.sleep(0.033)
#I use tread because it  can play 2 part of code separately(i learn it today llamo)
thread1 = Thread(target=play_sound)
thread2 = Thread(target=play_video)
thread1.start()
thread2.start()
