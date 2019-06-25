# -*- coding: utf-8 -*-

#机器人交互表情的简单显示方案
#明天考完试继续完善

import cv2

img = cv2.imread(r'C:\Users\Administrator\OneDrive\robocup\face\confused.png',0)

cv2.namedWindow('confused', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('confused',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.imshow('confused', img)
cv2.waitKey()
cv2.destroyAllWindows()
