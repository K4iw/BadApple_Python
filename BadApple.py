import numpy as np
from PIL import Image
import time
import sys
from playsound3 import playsound
from threading import Thread
#Value for resizing the img to fit in the terminal
height= 63
weight= 130

#Use to play soung
def play_sound():
    playsound("BadApple.mp3")

def data_image(path:str):
    """Get image array pixeldata"""
    image = Image.open(path)
    image = image.convert("L")
    #Resize the image
    image = image.resize((weight,height))
    return np.array(image)
def play_video():
    frame = 1
    printing = ""
    while frame < 6572:
        #Path to find the image
        path = f"frames/output_{frame:04}.jpg"
        #Call function data_image to get an array
        data =data_image(path)
        for y in range(height):
            printing+="\n"
            for x in range(weight):
                if data[y,x]<128:
                    printing +="/"
                else:
                    printing+="."
        #Next frame
        frame +=1
        #Print into the console (i have look online for alternative to print )
        time.sleep(0.03)
        sys.stdout.write(printing)
        #Reset the print
        printing =""

#I use tread because it  can play 2 part of code separately(i learn it today llamo)
thread1 = Thread(target=play_sound)
thread2 = Thread(target=play_video)
thread1.start()
if thread1.run :
    thread2.start()
