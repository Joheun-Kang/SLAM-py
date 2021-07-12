# feature precessing 
import cv2
import numpy as np
from skimage.transform import FundamentalMatrixTransform,EssentialMatrixTransform
from skimage.measure import ransac    

class extract_feature(object):

  def __init__(self,K):
    self.orb = cv2.ORB_create()
    self.bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
    self.last = None 
 
    self.K = K 
    self.Kinv = np.linalg.inv(self.K)
    
 
      

    
  def extract(self,frame,K):
    features = cv2.goodFeaturesToTrack(np.mean(frame,axis = 2).astype(np.uint8),3000,qualityLevel = 0.01, minDistance = 2)  
     
    kps = [cv2.KeyPoint(x = f[0][0], y = f[0][1], _size = 20) for f in features]
    kps, des = self.orb.compute(frame,kps)
    
    matches = None
    matching_pts = []
        

    # find matching points 
    bf = cv2.BFMatcher()
    if self.last != None:
      matches = bf.knnMatch(des,self.last['des'],k=2)
        
      for m,n in matches:
        if m.distance < 0.65*n.distance:
          kp1 = kps[m.queryIdx].pt
          kp2 = self.last['kps'][m.trainIdx].pt 
          matching_pts.append((kp1, kp2))
        
    if len(matching_pts)>0:
      matching_pts = np.array(matching_pts)

      # with the matching points, we find the "keymatching" points
      # from this ransac, we find the homography
      model,inliers = ransac((matching_pts[:,0],matching_pts[:,1]),EssentialMatrixTransform,min_samples = 8,residual_threshold = 1,max_trials = 120)

      print('essential model param from ransac',model.params)
          
      # this is better matching 'key' points
      matching_pts= matching_pts[inliers]


        

    self.last = {'kps':kps , 'des':des}
        
    return kps,np.array(matching_pts)
       




    
