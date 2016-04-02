import numpy as np
import cv2

def extractFG(img,x,y,w,h):
	
	x = x - int(w * 0.15)
    	y = y - int(h * 0.15)
    	w = w + int(w * 0.15)
    	h = h + int(h * 0.25)
	
	

	rect = (x,y,w,h) #Region Of Interest

	mask = np.zeros(img.shape[:2],dtype = np.uint8)

	bgdmodel = np.zeros((1,65),np.float64)

	fgdmodel = np.zeros((1,65),np.float64)

	eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	roi_gray = gray[y:y+h,x:x+w]

	roi_mask = mask[y:y+h,x:x+w]

	eyes = []

	eyes = eye_cascade.detectMultiScale(roi_gray)

	print(eyes)

	cv2.grabCut(img,mask,rect,bgdmodel,fgdmodel,1,cv2.GC_INIT_WITH_RECT)
	
	for(ex,ey,ew,eh) in eyes:
		eh = eh + (int(eh) * 2)
		cv2.rectangle(roi_mask,(ex,ey),(ex+ew,ey+eh),1,-1)

	cv2.grabCut(img,mask,rect,bgdmodel,fgdmodel,1,cv2.GC_INIT_WITH_MASK)
	mask2 = np.where((mask==1) + (mask == 3),255,0).astype('uint8')
	
	output = cv2.bitwise_and(img,img,mask=mask2)

	#cv2.rectangle(output,(x,y),(x+w,y+h),(255,0,255),2)

 	return output
