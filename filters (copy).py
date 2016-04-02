import Image
import numpy as np
import cv2
from PIL import Image
'''
img = Image.new( 'RGB', (255,255), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = (i, j, 100) # set the colour accordingly

img.show(img)

#print(img)
#cv2.imshow('image', img)

'''

'''
img = Image.open('shakira.jpg')
width = img.size[0]
height = img.size[1]
print(width,height)
img2 = Image.new('RGB', (width, height), "black")# creates a new image for manipulation
newpixels = img2.load()# creates a new pixel map
#img2.show()# for some reason it does not show the image.

#print(img.size)

#print(img.format)

for i in range(width):    # for every pixel:
    for j in range(height):
	color = img.getpixel((i,j))
	red = color[0]
	green = color[1]
	blue = color[2]
	
	#print(newpixels[i,j])
	if(red == 0 and green ==0 and blue == 0):
		newpixels[i,j] = (red, green, blue)
	else:
		#manipulation of the new image is done here
		newpixels[i,j] = (64,224,208)
	
	#print(red,green,blue)
'''
'''
MAKING SURE THE PIXELS ARE BEING PASSED ON TO ANOTHER IMAGE
for i in range(width):    # for every pixel:
    for j in range(height):
	color2 = img2.getpixel((i,j))
	red2 = color2[0]
	green2 = color2[1]
	blue2 = color2[2]

	print(red2, green2, blue2)


img2.show()
img2.save('shakira2.png')
'''


def filterAlgorithm1(img):
#img = Image.open('shakira.jpg')
	width = img.size[0]
	height = img.size[1]
	print(width,height)
	img2 = Image.new('RGB', (width, height), "black")# creates a new image for manipulation
	newpixels = img2.load()# creates a new pixel map
#img2.show()# for some reason it does not show the image.

#print(img.size)

#print(img.format)

	for i in range(width):    # for every pixel:
    		for j in range(height):
			color = img.getpixel((i,j))
			red = color[0]
			green = color[1]
			blue = color[2]
	
	#print(newpixels[i,j])
			if(red == 0 and green ==0 and blue == 0):
				newpixels[i,j] = (red, green, blue)
			else:
		#manipulation of the new image is done here
				#newpixels[i,j] = (red-100,green+100,blue-100)
				if(red > 50 and green > 50 and blue >50):
					newpixels[i,j] = (red-100,green+100,blue-100)
	
	#print(red,green,blue)
	img2.save('testmanipulation.jpg')

def filterAlgorithm2(img):
#img = Image.open('shakira.jpg')
	width = img.size[0]
	height = img.size[1]
	print(width,height)
	img2 = Image.new('RGB', (width, height), "black")# creates a new image for manipulation
	newpixels = img2.load()# creates a new pixel map
#img2.show()# for some reason it does not show the image.

#print(img.size)

#print(img.format)

	for i in range(width):    # for every pixel:
    		for j in range(height):
			color = img.getpixel((i,j))
			red = color[0]
			green = color[1]
			blue = color[2]
	
	#print(newpixels[i,j])
			if(red == 0 and green ==0 and blue == 0):
				newpixels[i,j] = (red, green, blue)
			else:
		#manipulation of the new image is done here
				if(red > 50 and green > 50 and blue >50):
					newpixels[i,j] = (red+100,green-100,blue-100)
	
	#print(red,green,blue)
	img2.save('testmanipulation.jpg')

def filterAlgorithm3(img):
#img = Image.open('shakira.jpg')
	width = img.size[0]
	height = img.size[1]
	print(width,height)
	img2 = Image.new('RGB', (width, height), "black")# creates a new image for manipulation
	newpixels = img2.load()# creates a new pixel map
#img2.show()# for some reason it does not show the image.

#print(img.size)

#print(img.format)

	for i in range(width):    # for every pixel:
    		for j in range(height):
			color = img.getpixel((i,j))
			red = color[0]
			green = color[1]
			blue = color[2]
	
	#print(newpixels[i,j])
			if(red == 0 and green ==0 and blue == 0):
				newpixels[i,j] = (red, green, blue)
			else:
		#manipulation of the new image is done here
				if(red > 50 and green > 50 and blue >50):
					newpixels[i,j] = (red -100,green-100,blue+100)
	
	#print(red,green,blue)
	img2.save('testmanipulation.jpg')


img = Image.open('test1.jpg')
filterAlgorithm1(img)





























