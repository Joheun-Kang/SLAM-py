import numpy as np
import cv2
import pygame
import sys
import skimage
from pygame.locals import DOUBLEBUF
from feature import extract_feature, create_hmg, normalize

from display import Display2D


w = 640
h = 480

disp2d = Display2D(w,h)
F = 909
K = np.array([[F,0,w//2],[0,F,h//2],[0,0,1]])  
<<<<<<< HEAD

fe = extract_feature(K)



def image_process(frame):
  # get goot match points (not normalized )
  kps, matching_pts= fe.extract(frame,K) 
  
  
  for pts1, pts2 in matching_pts:
    u1,v1 = map(lambda x: int(round(x)),pts1)
    u2,v2 = map(lambda x: int(round(x)),pts2)
    
=======

fe = extract_feature(K)
>>>>>>> d9844f33de3761dedf0138eeae8165c2b8436ea0

    

    cv2.circle(frame, (u1,v1), color = (0,255,0),radius = 3)
    cv2.line(frame, (u1,v1),(u2,v2), color = (255,0,0))

  return frame



def image_process(frame):
    matched_pts = fe.extract(frame)
    
    for pt1, pt2 in matched_pts:
        
        #print((pt1,pt2))
        u1,v1 = map(lambda x: int(round(x)),pt1)
        u2,v2 = map(lambda x: int(round(x)),pt2)
        #u1,v1 = fe.denormalize(pt1) # need to come back to original drawing points
        #u2,v2 = fe.denormalize(pt2)

        # manually denormalize for display
        u1 += frame.shape[0]//2
        u2 += frame.shape[0]//2
        v1 += frame.shape[1]//2
        v2 += frame.shape[1]//2


        cv2.circle(frame, (u1,v1), color = (0,255,0),radius = 3)
        cv2.line(frame, (u1,v1),(u2,v2), color = (255,0,0))

    return frame



<<<<<<< HEAD
if  __name__ == '__main__':
  cap = cv2.VideoCapture('/Users/joheunkang/Desktop/mini_SLAM/videos/ex2.mp4')                
  while cap.isOpened():
    ret,frame = cap.read()
    frame = cv2.resize(frame,(w,h))
    frame= image_process(frame)

    if ret ==True:
      disp2d.draw(frame)
    else:
      break
=======



if  __name__ == '__main__':
    
    cap = cv2.VideoCapture('/Users/joheunkang/Desktop/mini_SLAM/videos/ex2.mp4')
        
    while cap.isOpened():
        ret,frame = cap.read()
        frame = cv2.resize(frame,(w,h))
        
        frame= image_process(frame)

          
        if ret == True:
            disp2d.draw(frame)
        else:
           break
>>>>>>> d9844f33de3761dedf0138eeae8165c2b8436ea0
