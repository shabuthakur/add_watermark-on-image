#!/usr/bin/env python
# coding: utf-8

# In[30]:


from moviepy.editor import *
import cv2


# In[31]:


clip = VideoFileClip(r'C:\Users\hp\Desktop\vedios\2.mp4')


# In[32]:


img=cv2.imread(r"C:\Users\hp\Desktop\watermark\images\1.jpg")


# In[33]:


h_img, w_img,_= img.shape
w_clip,h_clip=clip.size


# In[34]:


print(h_img, w_img)


# In[35]:


center_y=int(h_clip/2)
center_x=int(w_clip/2)
top_y=center_y-int(h_img/2)
left_x = center_x- int(w_img/2)
bottom_y= top_y+h_img
right_x=left_x+w_img


# In[36]:



#img[top_y:bottom_y,left_x:right_x] = logo


txt_clip=ImageClip(img)

txt_clip=txt_clip.set_position((20,20)).set_duration(clip.duration)


# In[ ]:





# In[37]:



video = CompositeVideoClip([clip,txt_clip.set_start(2).crossfadein(3)])


# In[ ]:





# In[38]:


video.ipython_display(width=350)


# In[ ]:




