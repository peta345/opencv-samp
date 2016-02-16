#coding: utf-8
import cv2

#二値化するために画像＞グレースケール変換
#する必要がある。

img = cv2.imread("./hoge.jpg")
#or img = cv2.imread("hoge.jpg", cv2.CV_LOAD_IMAGE_GRAYSCALE)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite("poko.jpg", im_bw)
