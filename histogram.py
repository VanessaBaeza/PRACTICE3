import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/vanessa/Documents/VISION/PRACTICA3/Moritz.jpg')

answer = None
while answer not in ("gray", "blue", "red", "green", "none","bi"):
    answer = raw_input("Which histogram do you want? (gray, blue, red, green or bi -for binarization-) \n")
    if answer == "blue":
        histr = cv2.calcHist([img],[0],None,[256],[0,256])
        plt.plot(histr,'b')
        plt.xlim([0,256])
        plt.show()
    if answer == "green":
        histr = cv2.calcHist([img],[1],None,[256],[0,256])
        plt.plot(histr,'g')
        plt.xlim([0,256])
        plt.show()
    if answer == "red":
        histr = cv2.calcHist([img],[2],None,[256],[0,256])
        plt.plot(histr,'r')
        plt.xlim([0,256])
        plt.show()
    if answer == "bi":
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        
        titles = ['Original Image','BINARY']
        images = [img, thresh]
        for i in xrange(2):
            plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])
        plt.show()
    elif answer == "gray":
        plt.hist(img.ravel(),256,[0,256]); plt.show()
    else:
        print("Please enter gray, blue, red, green or none")


        
