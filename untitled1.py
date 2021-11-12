# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 10:05:02 2021

@author: hp
"""

import cv2

#this function in basically used for resize the image
def scale(image, scale_width):
    (image_height, image_width)=image.shape[:2]
    new_height = int(scale_width / image_width * image_height)
    return cv2.resize(image,(scale_width,new_height))


logo=scale(cv2.imread(r"C:\Users\hp\Desktop\watermark\images\1.jpg"),100)
h_logo, w_logo,_= logo.shape

img=scale(cv2.imread(r"C:\Users\hp\Desktop\watermark\images\2.jpg"),400)
h_img, w_img,_= img.shape

center_y=int(h_img/-14)
center_x=int(w_img/-7)
top_y=center_y-int(h_logo/2)
left_x = center_x- int(w_logo/2)
bottom_y= top_y+h_logo
right_x=left_x+w_logo
#cv2.circle(img,(center_y,center_x),10,(0,255,0),-1)
#cv2.circle(img,(left_x,top_y),10,(0,255,0),-1)
#cv2.circle(img,(right_x,bottom_y),10,(0,255,0),-1)


#get RoI
roi = img[top_y:bottom_y,left_x:right_x]
#img[top_y:bottom_y,left_x:right_x] = logo

result=cv2.addWeighted(roi,1,logo,0.3,0)
img[top_y:bottom_y,left_x:right_x] = result
cv2.imshow("result",result)
cv2.imshow("image",img)
cv2.imshow("logo",logo)
cv2.imshow("rio",roi)
cv2.waitKey(0)