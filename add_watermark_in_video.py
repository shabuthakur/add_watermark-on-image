#!/usr/bin/env python
# coding: utf-8



from moviepy.editor import *
import cv2

clip = VideoFileClip(r'C:\Users\hp\Desktop\vedios\2.mp4')

img=cv2.imread(r"C:\Users\hp\Desktop\watermark\images\1.jpg")

h_img, w_img,_= img.shape
w_clip,h_clip=clip.size

print(h_img, w_img)

center_y=int(h_clip/2)
center_x=int(w_clip/2)
top_y=center_y-int(h_img/2)
left_x = center_x- int(w_img/2)
bottom_y= top_y+h_img
right_x=left_x+w_img


txt_clip=ImageClip(img)

txt_clip=txt_clip.set_position((20,20)).set_duration(clip.duration)

video = CompositeVideoClip([clip,txt_clip.set_start(2).crossfadein(3)])


video.ipython_display(width=350)





