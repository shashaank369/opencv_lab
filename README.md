# opencv_lab
import cv2

img = cv2.imread(r"X:\opencv\downloads.jpg")

if img is None:
    print("❌ Image not loaded")
    exit()

resized = cv2.resize(img, (400, 300))
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blur, 100, 200)

cv2.imshow("Original", img)
cv2.imshow("Resized", resized)
cv2.imshow("Gray", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
