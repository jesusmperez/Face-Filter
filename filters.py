import Image
import numpy as np
import cv2
from PIL import Image
import PIL.Image

from Tkinter import *
from tkFileDialog import askopenfilename
import Tkinter
import tkFileDialog



check = 1


def filterAlgorithm1():
#img = Image.open('shakira.jpg')
	
	#print(check)
	global check
	
	originalIm = PIL.Image.open('COPY.jpg')
	originalIm.show()
	#imgz = PIL.Image.open('vale'+ str(check) + '.jpg')
	

	
	imgz = PIL.Image.open('vale'+ str(check) + '.jpg')
	check  =  check+1
	
	

	
	
	width = imgz.size[0]
	height = imgz.size[1]
	print(width,height)
	#img2 = Image.new('RGB', (width, height), "black")# creates a new image for manipulation
	newpixels = originalIm.load()# creates a new pixel map
#img2.show()# for some reason it does not show the image.

#print(img.size)

#print(img.format)

	for i in range(width):    # for every pixel:
    		for j in range(height):
			color = imgz.getpixel((i,j))
			red = color[0]
			green = color[1]
			blue = color[2]
	
	#print(newpixels[i,j])
			if(red == 0 and green ==0 and blue == 0):
				noChange = originalIm.getpixel((i,j))
				red2 = noChange[0]
				green2 = noChange[1]
				blue2 = noChange[2]
			else:
				if(red > 35 and green > 20 and blue > 30):
					newpixels[i,j] = (red+100,green-100,blue-100)
				
	
	#print(red,green,blue)
	originalIm.save('COPY.jpg')
	
	
def filterAlgorithm2():
#img = Image.open('shakira.jpg')

	#print(check)
	global check
	
	originalIm = PIL.Image.open('COPY.jpg')
	#imgz = PIL.Image.open('vale'+ str(check) + '.jpg')
	

	
	imgz = PIL.Image.open('vale'+ str(check) + '.jpg')
	check  =  check+1
	
	width = imgz.size[0]
	height = imgz.size[1]
	print(width,height)
	#img2 = Image.new('RGB', (width, height), "black")# creates a new image for manipulation
	newpixels = originalIm.load()# creates a new pixel map
#img2.show()# for some reason it does not show the image.

#print(img.size)

#print(img.format)

	for i in range(width):    # for every pixel:
    		for j in range(height):
			color = imgz.getpixel((i,j))
			red = color[0]
			green = color[1]
			blue = color[2]
	
	#print(newpixels[i,j])
			if(red == 0 and green ==0 and blue == 0):
				noChange = originalIm.getpixel((i,j))
				red2 = noChange[0]
				green2 = noChange[1]
				blue2 = noChange[2]
			else:
				if(red > 35 and green > 20 and blue > 30):
					newpixels[i,j] = (red-100,green+100,blue-100)
				
	
	#print(red,green,blue)
	originalIm.save('COPY.jpg')

def filterAlgorithm3():
#img = Image.open('shakira.jpg')





	#print(check)
	global check
	
	originalIm = PIL.Image.open('COPY.jpg')
	#imgz = PIL.Image.open('vale'+ str(check) + '.jpg')
	

	
	imgz = PIL.Image.open('vale'+ str(check) + '.jpg')
	check  =  check+1
	
	

	width = imgz.size[0]
	height = imgz.size[1]
	print(width,height)
	#img2 = Image.new('RGB', (width, height), "black")# creates a new image for manipulation
	newpixels = originalIm.load()# creates a new pixel map
#img2.show()# for some reason it does not show the image.

#print(img.size)

#print(img.format)

	for i in range(width):    # for every pixel:
    		for j in range(height):
			color = imgz.getpixel((i,j))
			red = color[0]
			green = color[1]
			blue = color[2]
	
	#print(newpixels[i,j])
			if(red == 0 and green ==0 and blue == 0):
				noChange = originalIm.getpixel((i,j))
				red2 = noChange[0]
				green2 = noChange[1]
				blue2 = noChange[2]
			else:
				if(red > 35 and green > 20 and blue > 30):
					newpixels[i,j] = (red-100,green-100,blue+100)
				
	
	#print(red,green,blue)
	originalIm.save('COPY.jpg')

def filterAlgorithm4():
	
	global check
	
	originalIm = PIL.Image.open('COPY.jpg')
	#imgz = PIL.Image.open('vale'+ str(check) + '.jpg')
	

	
	imgz = PIL.Image.open('vale'+ str(check) + '.jpg')
	check  =  check+1
	
	


	im = PIL.Image.open(getFile("choose an image to blend"))

	width = imgz.size[0]
	height = imgz.size[1]
	
	newBlend = im.resize((width,height))
	
	
	
	

	test = PIL.Image.blend(newBlend, imgz, 0.5)
	test.save('hello.jpg')
	newBlends = test.load()
	
	
	
	
	
	newpixels = originalIm.load()# creates a new pixel map


	for i in range(width):    # for every pixel:
    		for j in range(height):
			color = imgz.getpixel((i,j))
			color2 = test.getpixel((i,j))
			
			red = color[0]
			green = color[1]
			blue = color[2]
			red2 = color2[0]
			green2 = color2[1]
			blue2 = color2[2]
	
	#print(newpixels[i,j])
			if(red == 0 and green ==0 and blue == 0):
				noChange = originalIm.getpixel((i,j))
				red2 = noChange[0]
				green2 = noChange[1]
				blue2 = noChange[2]
			else:
				if(red > 35 and green > 20 and blue > 30):
					newpixels[i,j] = (red2,green2,blue2)
				
	
	#print(red,green,blue)
	originalIm.save('COPY.jpg')
	
def getFile(message):
	'''
	getFile(message):
	This function takes in a string then promts to open a file with a file window.
	This function returns the file path.
	'''
	fileFortmats =["jpg","jpeg","png"] #list of formats to check for a valid file
	isnotValid = True #boolean to keep track of valid file formats
	count = 0 #variable to keep track of how many times the user tried to open an invalid file type

	while(isnotValid):
		file = Tkinter.Tk()
		file.withdraw()
		filename = tkFileDialog.askopenfilename(parent=file, title=message) #prompt user to open an image file
		for formats in fileFortmats: #check file format
			if(filename.find(formats) > 0):
				isnotValid = False

		if(isnotValid): #give error message
			message = "Invalid file format. Please choose an image."
		count = count + 1
		
		if(count > 5):
			print("Sorry, could not open files of that type, goodbye.")
			exit() #if user makes a lot of invalid selections

	return filename

	





























