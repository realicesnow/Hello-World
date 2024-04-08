import cv2
import numpy as np


img = cv2.imread("./image.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("image_gray.png", gray)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=100, param2=40, minRadius=1, maxRadius=50)

circles = np.uint16(np.around(circles))

for circle in circles[0, :]:
    # 円周を描画する
    cv2.circle(img, (circle[0], circle[1]), circle[2], (0, 165, 255), 3)
    # 中心点を描画する
    cv2.circle(img, (circle[0], circle[1]), 2, (0, 0, 255), 3)

cv2.imwrite("image_after.png", img)