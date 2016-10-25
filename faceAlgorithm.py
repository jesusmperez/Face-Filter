
import numpy as np
import cv2
#from PIL import Image, ImageFilter
from matplotlib import pyplot as plt
from filters import *
from coleman import *

import PIL.Image

from Tkinter import *
from tkFileDialog import askopenfilename
import Tkinter
import tkFileDialog



def isTrue(crop_image, counterf, truex, truey, truew, trueh):
	
	check = counterf
	
	
	#print(check)
	#crop_image = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
	cv2.imwrite('vale'+ str(check) + '.jpg', crop_image)
	img = cv2.imread('COPY.jpg' )
	#cv2.imwrite('cut.jpg', crop_image)
	#cutout = Image.open('cut.jpg')
	
	x = truex
	y = truey
	w = truew
	h = trueh
	
	img = extractFG(img,x,y,w,h)
	
	


	cv2.imshow('img', img)
	cv2.imwrite('vale'+ str(check) + '.jpg', img)
	
	# SO WE GET VALE1 AND VALE2 FROM THIS
	#print('SAVING IMAGES')
	
	#imgz = PIL.Image.open('vale'+ str(check) + '.jpg')
	def quit():
		master.quit()
	master = Tk()
	master.title("Choose a filter")
	master.geometry ("400x250")

	topFrame = Frame(master)
	topFrame.pack()

	button1 = Button(topFrame, text = "Red", fg = "red", command = filterAlgorithm1)

	button2 = Button(topFrame, text = "Green", fg = "green", command = filterAlgorithm2)
	button3 = Button(topFrame, text = "Blue", fg = "blue", command = filterAlgorithm3)
	button4 = Button(topFrame, text = "Blend", fg = "black", command = filterAlgorithm4)
	quit = Button(topFrame, text = "next", fg = "black", command = quit)
	
	



	button1.grid(row = 0, sticky = E)
	button2.grid(row = 1, sticky = E)
	button3.grid(row= 2, sticky = E)
	button4.grid(row = 3, sticky = E)
	quit.grid( row = 4, sticky = E)

	

	master.mainloop()

	
	
	
	#filterAlgorithm2(imgz, originalIm)
	#print('THIS IS HOW MANY TIMES IT OPENS THE IMAGE',check)
	

	


	

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# lets the user pick an image.

file = Tkinter.Tk()
file.withdraw()
filename = tkFileDialog.askopenfilename(parent=file)
# This is where I will bring the place as to where the user will set the image.


img = cv2.imread(filename)

cv2.imwrite('COPY.jpg', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow('image', gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

############################################################################################################

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

counter1 = 0
counter2 = 0


#print(faces[0])
#print(faces[1])
#print(counter1)



for (x,y,w,h) in faces:
    counter1 = counter1+1
   

    #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+(h), x:x+(w)]

    #print("gray", roi_gray)
    

    roi_color = img[y:y+(h/2+ 55), x:x+(w)]
    #crop_img = roi_color
   
   
    eyes = eye_cascade.detectMultiScale(roi_gray)
    
  
    
    for (ex,ey,ew,eh) in eyes:
    	#cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	counter2 = counter2+1
	#print(counter2)
print("TESTING UNDER HERE")
list1 = []
list2 = []





#img2 = cv2.imread('obama-best.jpg')
gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


onef = 0
twof = 0
threef = 0
fourf = 0

onee = 0
twoe = 0
threee = 0
foure = 0

truex = 0
truey = 0
truew = 0
trueh = 0

counterf = 0

for (fx, fy, fw, fh) in (faces):
     counterf = counterf + 1
     #print(counterf)
     

     #print(fx,fy,fw,fh)
     onef = fx
     twof = fy
     threef = fw
     fourf = fh
     
     print("FACES")
     print(onef, twof, threef, fourf)
     roi_gray2 = gray2[fy:fy+(fh), fx:fx+(fw)]
     
     eyes2 = eye_cascade.detectMultiScale(roi_gray2)
     


     
     for(xe, ye, we, he) in (eyes2):
	
	 onee = xe
	 twoe = ye
	 threee = we
	 foure = he
	
		
	 print("EYES")
	 print(onee, twoe, threee, foure)
     if(threef > threee):
		truex = onef
		truey = twof
		truew = threef
		trueh = threef

		print("THIS IS THE TRUE FACE COORDINATES", truex, truey, truew, trueh)
		crop_image = img[truey:truey+trueh, truex:truex+truew]
		
		print('PASSES')
		isTrue(crop_image, counterf, truex, truey, truew, trueh)



# CHANGES DONE BELOW THIS LINE
    
##############################################################################################################

    
    

#print(roi_gray)
##################################################################################################
#TESTING FOR MOUTH DETECTION
# CODE SHOWS A LOT OF RECTANGLES ACROSS THE FACE.
"""

for (x,y,w,h) in faces:

    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+(h), x:x+(w)]
    

    roi_color = img[y:y+(h), x:x+(w)]
    
   # print(crop_img)
	
   
    smile = smile_cascade.detectMultiScale(roi_gray)
    for(xe, ye, we, hw) in smile:
	cv2.rectangle(roi_color, (xe, ye), (xe+we, ye+hw), (0, 0, 0), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
"""



#cv2.startWindowThread()
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
################# CODE MANIPULATION STARTS HERE

#crop_img = img[400:800, 200:600]# CODE WORKS NEED TO GRAB CERTAIN POINTS TO GET A IMAGE AT A CERTAIN X,Y LOCATION!
#cv2.imshow('image', crop_img)
#cv2.waitKey(0)



"""
CODE TO SHOW ORIGINAL IMAGE WITH FACE DETECTION ALGORITHM.	

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
"""
ORIGINAL CODE TO CROP IMAGE

img = cv2.imread("")
crop_img = img[200:400, 100:300] # Crop from x, y, w, h -> 100, 200, 300, 400
# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
"""

	





