import cv2
img = cv2.imread("Rc2026.jpg")
if img is None:
    print("Image not found!")
    exit()
flip_vertical = cv2.flip(img, 0)
flip_horizontal = cv2.flip(img, 1)
flip_both = cv2.flip(img, -1)
cv2.imshow("Original", img)
cv2.imshow("Vertical Flip", flip_vertical)
cv2.imshow("Horizontal Flip", flip_horizontal)
cv2.imshow("Both Flip", flip_both)
cv2.waitKey(0)
cv2.destroyAllWindows()
