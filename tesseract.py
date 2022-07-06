import pytesseract
import argparse
import cv2
from preprocessing import *

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gray = get_grayscale(image)
threshold = thresholding(gray)
opening = opening(gray)
canny = canny(gray)

# images = [image, gray, threshold, opening, canny]
images = [image]

custom_config = r"--oem 3 --psm 6"

for i in images:
    # text = pytesseract.image_to_string(i, config=custom_config)
    # print(text)
    # print("----")
    h, w, c = i.shape
    boxes = pytesseract.image_to_boxes(i)
    for b in boxes.splitlines():
        b = b.split(" ")
        i = cv2.rectangle(
            i, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2
        )
    cv2.imshow("img", i)
    cv2.waitKey(0)
