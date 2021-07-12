import numpy as np
import cv2
import pygame
import sys
import skimage
from pygame.locals import DOUBLEBUF
from feature import extract_feature

from display import Display2D


w = 640
h = 480

disp2d = Display2D(w,h)
F = 270
K = np.array([[F,0,w//2],[0,F,h//2],[0,0,1]])  


fe = extract_feature(K)

def create_hmg(pts):
  n = pts.shape[0]
  return np.concatenate([pts,np.ones(1)],axis= 0)

def normalize(K,pt):
  # modeul eror : we can not return and use normalized , need to define one varialbe 
  normalized = np.dot(np.linalg.inv(K),pt)
  return normalized

def image_process(frame):
  # get goot match points (not normalized )
  kps, matching_pts= fe.extract(frame,K)

  
  
  for pts1, pts2 in matching_pts:
    
    # add hmg + normalize with inverse(intrinsic) maxtix mul
    pts1_hmg = create_hmg(pts1)
    pts2_hmg = create_hmg(pts2)

    # noramlized points 
    pts1_n = normalize(K,pts1_hmg)[:2]
    pts2_n = normalize(K,pts2_hmg)[:2]
  
    u1,v1 = map(lambda x: int(round(x)),pts1)
    u2,v2 = map(lambda x: int(round(x)),pts2)
  
    cv2.circle(frame, (u1,v1), color = (0,255,0),radius = 3)
    cv2.line(frame, (u1,v1),(u2,v2), color = (255,0,0))

  return frame


if  __name__ == '__main__':
  cap = cv2.VideoCapture('/Users/joheunkang/Desktop/fun/videos/test_countryroad.mp4')                
  while cap.isOpened():
    ret,frame = cap.read()
    frame = cv2.resize(frame,(w,h))
    frame= image_process(frame)

    if ret ==True:
      disp2d.draw(frame)
    else:
      break




