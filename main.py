#!/usr/bin/env python
# coding: utf-8




# In[1]:


import cv2 #opencv
import os
import time
import uuid


# In[2]:


IMAGES_PATH = "alif"


# In[3]:
"""
    TODO:
        o 


"""


labels = ["b"]
number_imgs=20


# In[4]:


# address = "http://192.168.0.101:8080/video"
# cap.open(address)
for label in labels:
    os.mkdir(f"{IMAGES_PATH}/"+label)
    
    cap = cv2.VideoCapture(0)
    print("Collecting Images for {}".format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        
        ret,frame = cap.read()
        # frame = cv2.resize(frame,(852,480),fx=0,fy=0,interpolation=cv2.INTER_CUBIC)
        imagename = os.path.join(IMAGES_PATH,label,label+".{}.jpg".format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow("frame",frame)
        time.sleep(2)
        if cv2.waitKey(1) & 0xff== ord("q"):
            break
    cap.release()
    


# In[ ]:




