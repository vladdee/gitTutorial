import cv2
import numpy

def cvimg_to_list(image):
    """Same exact function only using list comprehension instead"""
    conv_list = [tuple(image[i, j])
                for i in range(image.shape[0])
                for j in range(image.shape[1])]
    return conv_list

def hsvlist_to_array(lst, width):
    img = []
    for i, x in enumerate(lst):
        if i % width == 0:
            img.append([x])
        else:
            img[-1].append(x)
    img_np = numpy.asarray(img, numpy.uint8)
    return img_np

def generator_from_image(img):
    def generator(i):
        return img[i]
    return generator

original_img = cv2.imread("plane.jpg")
original_list = cvimg_to_list(original_img)

generator = generator_from_image(original_list)

new_list = [generator(i) for i in range(len(original_list))]

cv2.imshow('original', original_img)
cv2.waitKey(0)
cv2.imshow('new', hsvlist_to_array(new_list, 640))
cv2.waitKey(0)
