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
            return 1
        else:
            return 0
    return checker

def generator1():
    if random.random() > 0.99:
        return (0, 0, 255)
    else:
        return (0, 0, 0)

def hsvlist_to_array(lst, width):
    img = []
    for i, x in enumerate(lst):
        if i % width == 0:
            img.append([x])
        else:
            img[-1].append(x)
    img_np = numpy.asarray(img, numpy.uint8)
    return img_np

def gradient_condition():
    def condition(tupl):
        if all(x == 255 for x in tupl):
            return 1
        elif all(x == 0 for x in tupl):
            return 0
        else:
            return tupl[2]/256
    return condition

grad_rgb_list = cvimg_to_list(cv2.imread("gradient.jpg"))
plane_rgb_list = cvimg_to_list(cv2.imread("plane.jpg"))
flowers_rgb_list = cvimg_to_list(cv2.imread("flowers.jpg"))

rgb = grad_rgb_list
mask_func = gradient_condition()
gen2 = generator_from_image(plane_rgb_list)
gen1 = generator_from_image(flowers_rgb_list)

def combine_images(mask, mask_function, gen1, gen2):    
    blended = []
    for i, x in enumerate(mask):
        cond1 = mask_function(x)
        cond2 = 1 - mask_function(x)
        blended.append((gen1(i)[0]*cond1 + gen2(i)[0]*cond2, gen1(i)[1]*cond1 + gen2(i)[1]*cond2, gen1(i)[2]*cond1 + gen2(i)[2]*cond2))
    image = hsvlist_to_array(blended, 640)
    cv2.imshow("blended", image)
    cv2.waitKey(0)
