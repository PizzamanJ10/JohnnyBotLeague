
# Importing Image class from PIL module
from PIL import Image
from FindText import getText
 
# Opens a image in RGB mode
im = Image.open("test.png")
 
 
#here we have cropped images, which we will use to extract data from
champ_stats_left = im.crop((865, 1570, 950, 1715))

#all functions to get stats
def get_ad():

    toReturn = ""

    for letter in getText(champ_stats_left):

        if letter == '\n':
            break
        else:
            toReturn = toReturn + letter

    return toReturn

