import numpy as np
import glob #retrive file path and path name
import matplotlib.pyplot as plt
import imageio.v3 as iio  #provides an easy interface to read and write a wide range of image data
import skimage.color 
import skimage.filters



def auto_x(image):
    #image = iio.imread(uri="C:/Users/Admin/Desktop/IIT Indore assignment/CV Project/images/a1.jpg")
    fig, ax = plt.subplots()
    plt.imshow(image)

    # convert the image to grayscale
    gray_image = skimage.color.rgb2gray(image)

    # blur the image to denoise
    blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)

    # show the histogram of the blurred image
    histogram, bin_edges = np.histogram(blurred_image, bins=256, range=(0.0, 1.0))
    fig, ax = plt.subplots()
    plt.plot(bin_edges[0:-1], histogram)
    plt.title("Graylevel histogram")
    plt.xlabel("gray value")
    plt.ylabel("pixel count")
    plt.xlim(0, 1.0)

    # perform automatic thresholding
    t = skimage.filters.threshold_otsu(blurred_image)
    t=t*100
    x=round(abs(t))
    print(x)
    print("Found automatic threshold t = {}.".format(t))
    return x