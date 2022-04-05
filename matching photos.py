import numpy as np
import cv2
image = cv2.resize(cv2.imread("C://Krishay/mj.png", 0), (0, 0), fx=0.5, fy=0.5)
template = cv2.resize(cv2.imread("C:/Krishay/sheesh.png", 0), (0,0), fx=0.5, fy=0.5)

h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, 
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = image.copy()
    result = cv2.matchTemplate(img2, template, method)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in[cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    
    bottom_corner = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_corner, 255, 3)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()