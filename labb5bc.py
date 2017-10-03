import cv2, numpy, random


def cvimg_to_list(image):
    """Same exact function only using list comprehension instead"""
    conv_list = [tuple(image[i, j])
                for i in range(image.shape[0])
                for j in range(image.shape[1])]
    return conv_list

def generator_from_image(img):
    def generator(i):
        return img[i]
    return generator

def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    def checker(pixel):
        (h, s, v) = pixel
        if hlow < h < hhigh and slow < s < shigh and vlow < v < vhigh:
            return True
        else:
            return False
    return checker

def generator1(index):
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)

plane_rgb = cv2.imread("plane.jpg")
plane_hsv = cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_RGB2HSV)
condition = pixel_constraint(5, 30, 50, 255, 100, 255)
plane_hsv_list = cvimg_to_list(plane_hsv)
plane_rgb_list = cvimg_to_list(plane_rgb)

generator2 = generator_from_image(plane_rgb_list)

def combine_images(hsv_img, condition, gen1, gen2):
