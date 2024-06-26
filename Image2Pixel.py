import cv2
import matplotlib.pyplot as plt
import sys

img = cv2.imread("in.png")
print("Converting..")
aaa = open('out.txt', 'x')
aaa.close
for number in range(img.shape[0]):
    for numbera in range(img.shape[1]):
        f = open('out.txt', 'a', encoding='UTF-8')
        f.write(f"scr.DrawPixel({number}, {numbera}, Color({img[number,numbera][0]}, {img[number,numbera][1]}, {img[number,numbera][2]}));\n")
        f.close()