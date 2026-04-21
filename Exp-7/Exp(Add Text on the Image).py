import cv2

img = cv2.imread("Rc2026.jpg")

cv2.putText(
    img,
    "Open CV Lab",
    (50,50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0,255,0),
    2
   )

cv2.imshow("Image With Text",img)

cv2.waitkey(0)
cv2.destroyAllWindows()
