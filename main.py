import argparse
import cv2
import numpy as np
import time

def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

for i in range(1,31):

    img_num = "./defect-all/" + str(i) + ".jpg"
    print(img_num)

    image = cv2.imread(img_num)

    #image = cv2.resize(image,(500,500))
    #cv2.imshow("windows_name", image)

    rotated90 = rotate(image, 90)
    #cv2.imshow("rotated90", rotated90)
    rotated90_text = "./defect-all/" + str(i) + "_2.jpg"
    cv2.imwrite(rotated90_text, rotated90)

    rotated180 = rotate(image, 180)
    rotated180_text = "./defect-all/" + str(i) + "_3.jpg"
    cv2.imwrite(rotated180_text, rotated180)
    #cv2.imshow("rotated180", rotated180)

    rotated270 = rotate(image, 270)
    rotated270_text = "./defect-all/" + str(i) + "_4.jpg"
    cv2.imwrite(rotated270_text, rotated270)
    # cv2.imshow("rotated270", rotated270)

    # Flipped Horizontally 水平翻转
    h_flip = cv2.flip(image, 1)
    h_flip_text = "./defect-all/" + str(i) + "_5.jpg"
    cv2.imwrite(h_flip_text, h_flip)

    # Flipped Vertically 垂直翻转
    v_flip = cv2.flip(image, 0)
    v_flip_text = "./defect-all/" + str(i) + "_6.jpg"
    cv2.imwrite(v_flip_text, v_flip)

    hv_flip = cv2.flip(image, -1)
    hv_flip_text = "./defect-all/" + str(i) + "_7.jpg"
    cv2.imwrite(hv_flip_text, hv_flip)

    cv2.waitKey(0)
    """

    # Flipped Horizontally & Vertically 水平垂直翻转
    hv_flip = cv2.flip(image, -1)
    cv2.imwrite("girl-hv.jpg", hv_flip)"""
