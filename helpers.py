import numpy as np
import cv2





def normalize(pts,K):
  # pts are from one frame and alreay 3d
  # return should be (3,1)
  return np.dot(np.linalg(K),pts)[0:2,:]
  
