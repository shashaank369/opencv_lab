import cv2

img = cv2.imread("Rc2026.jpg")

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("Original Image",img)
cv2.imshow("HSV Image",hsv)

cv2.waitkey(0)
cv2.destroyAllWindows()
