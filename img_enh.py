from PIL import Image,ImageEnhance,ImageStat
import math
import cv2
import numpy as np



def brightness(im_file):
    im = Image.open(im_file)
    stat = ImageStat.Stat(im)
    #finding the mean values, could use stat.rms for root mean sqaure values.
    r,g,b = stat.mean
    # gives the percieved brightness, using the formula involving mean values of RGB
    return math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))

def improve_image(im):
    #0 Finding the brightness level
    orglvl = brightness(im) #original level
    print(orglvl)

    #1 Brightness
    img = Image.open(im)
    #operating the brightness of image
    brght = ImageEnhance.Brightness(img)
    #enhancing the operated factor, where 1.0 returns original,>1 brightens
    if (orglvl<100): #taking rms value = 100 as standard for all images
        x = 100/orglvl
        brght_img = brght.enhance(x)
    else:
       brght_img = brght.enhance(1.0)
    #brght_img.show()
    #now saving the image
      #brtlvl = brightness(im) #after increasing brightness
    #print("after brightness:" + str(brtlvl))
                     

    #2 Sharpness
    # use the saved after the brightness changes
    img = Image.open(im)
    #operating the sharpness of image
    contrast = ImageEnhance.Sharpness(brght_img)
    #enhancing the operated factor, where 1.0 returns original,>1 increases sharpness
    shrp_img = contrast.enhance(1.0)
    
    #shrp_img.show()
    #now saving the image
     #shplvl = brightness(im) #after increasing sharpenss
    #print("after sharpness:"+str(shplvl))

     #3 Color
    # use the saved after the sharpness changes
    img = Image.open(im)
    #operating the color of image
    color = ImageEnhance.Color(shrp_img)
    #enhancing the operated factor, where 1.0 returns original,0.0 turns it into black and white
    clr_img = color.enhance(0.0)
    #clr_img.show()
    #now saving the image
    clr_img.save("final"+".jpg")
    clrlvl = brightness('final.jpg') #after increasing color
    print("after color:"+str(clrlvl))
    brtlvl = brightness('final.jpg') #after doing all changes
    print(brtlvl)
    #returning the image 
    return clr_img





improve_image('pic 1.jpg').show()



