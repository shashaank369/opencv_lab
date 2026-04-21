import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img_path = r"E:\Open Cv  (11239A003)\images.png"

if not os.path.exists(img_path):
    print("Error: Image path is incorrect")
    exit()

img = cv2.imread(img_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)

thresh = cv2.adaptiveThreshold(
    gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11, 2
)

custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(thresh, config=custom_config)

print("Detected Text:")
print(text)

cv2.imshow("Original Image", img)
cv2.imshow("Processed Image", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
