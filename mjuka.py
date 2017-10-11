import cv2, numpy, random

############################# Helpers ######################################
def cvimg_to_list(image):
    """
    Loops through all pixels in an image and returns a list of tuples with
    the pixel values
    """
    conv_list = [tuple(image[i, j])
                for i in range(image.shape[0])
                for j in range(image.shape[1])]
    return conv_list

def list_to_array(lst, width):
    """
    Creates and returns a numpyArray from a list of pixel value tuples
    and the picture's width
    """
    img = []
    for i, x in enumerate(lst):
        if i % width == 0:
            img.append([x])
        else:
            img[-1].append(x)
    img_np = numpy.asarray(img, numpy.uint8)
    return img_np

############################# Upgift C ########################################
def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """
    Creates and returns a function that checks if a
    given pixel value is within a certain given boundary
    """
    def checker(pixel):
        (h, s, v) = pixel
        if hlow < h < hhigh and slow < s < shigh and vlow < v < vhigh:
            return 1
        else:
            return 0
    return checker

def generator1(index):
    """
    99%  of the time returns a black pixel and 1%
    of the time returns a white pixel
    """
    if random.random() > 0.99:
        return (255, 255, 255)
    else:
        return (0, 0, 0)

############################# Uppgift D ######################################
def generator_from_image(img):
    """
    Creates and returns function that given a list with pixels and
    a position returns the pixel at the given position
    """
    def generator(i):
        return img[i]
    return generator

############################### Uppgift F ####################################
def gradient_condition():
    """
    Creates and returns a function that gives the grayscale
    value of a given pixel
    """
    def condition(pixel):
        if all(x == 255 for x in pixel):
            return 1
        elif all(x == 0 for x in pixel):
            return 0
        else:
            return pixel[2]/256
    return condition

############################### Inputs - Stars ###############################
grad_rgb_list = cvimg_to_list(cv2.imread("gradient.jpg"))
plane_rgb_list = cvimg_to_list(cv2.imread("plane.jpg"))
flowers_rgb_list = cvimg_to_list(cv2.imread("flowers.jpg"))

grad_mask = grad_rgb_list
grad_mask_func = gradient_condition()
grad_gen2 = generator_from_image(plane_rgb_list)
grad_gen1 = generator_from_image(flowers_rgb_list)

############################### Inputs - Soft ################################
plane_hsv = cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_RGB2HSV)
plane_hsv_list = cvimg_to_list(plane_hsv)
is_sky = pixel_constraint(5, 30, 50, 255, 100, 255)

stars_mask = [(255, 255, 255) if is_sky(x) == 0 else (0, 0, 0) for x in plane_hsv_list]
stars_mask_func = pixel_constraint(-1,1,-1,1,-1,1)
stars_gen2 = generator_from_image(plane_rgb_list)
stars_gen1 = generator1

############################# Uppgift E/F#####################################
def combine_images(mask, mask_function, gen1, gen2):
    """
    Combines two given pixels at a time according to the mask and
    mask function and creates a new openCV image
    """
    blended = []
    for i, x in enumerate(mask):
        cond1 = mask_function(x)
        cond2 = 1 - mask_function(x)
        wait = gen1(i)
        blended.append((wait[0]*cond1 + gen2(i)[0]*cond2,
                        wait[1]*cond1 + gen2(i)[1]*cond2,
                        wait[2]*cond1 + gen2(i)[2]*cond2))
    return blended
