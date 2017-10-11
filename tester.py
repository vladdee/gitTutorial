import cv2, numpy
from mjuka import *

if __name__ == "__main__":
    #pixel_constraint test
    checker = pixel_constraint(0,255,0,255,0,255)
    assert checker((1, 1, 1)) == 1
    assert checker((0, 0, 0)) == 0
    assert checker((1, 0, 1)) == 0
    print ("pixel constrain passed")
    #gradient_condition test
    condition = gradient_condition()
    assert condition((255, 255, 255)) == 1
    assert condition((0, 0, 0)) == 0
    assert condition((128, 128, 128)) == 0.5
    assert condition((200, 200, 200)) == (200/256)
    print ("gradient condition passed")
    #generator_from_image test
    img = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
    generator = generator_from_image(img)
    assert generator(0) == (1, 1, 1)
    assert generator(1) == (2, 2, 2)
    assert generator(2) == (3, 3, 3)
    print ("generator from image passed")
    #combine_images test
    mask = [(0,0,0), (255, 255, 255), (128, 128, 128), (255, 255, 255)]
    img1 = [(10, 10, 10), (100, 100, 100), (20, 20, 20), (200, 200, 200)]
    img2 = [(50, 50, 50), (75, 75, 75), (125, 125, 125), (150, 150, 150)]
    gen1 = generator_from_image(img1)
    gen2 = generator_from_image(img2)
    mask_func_1 = gradient_condition()
    res = [(50, 50, 50), (100, 100, 100), (72.5, 72.5, 72.5), (200, 200, 200)]
    assert combine_images(mask, mask_func_1, gen1, gen2) == res
    print ("combine images passed")
