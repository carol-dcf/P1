import os
# load and display an image with Matplotlib
from matplotlib import pyplot
from matplotlib import image

def bw_im(in_path, show):
    """
    Convert an image to black and white
    :param in_path: (str) path of input image
    :param show: (bool) visualize results
    :return:
    """
    out_path = "bw_" + in_path # Output path
    # FFMPEG command to convert an image to grayscale + compress it
    bw_command = "ffmpeg -i " + str(in_path) + " -vf format=gray -compression_level 100 " + str(out_path)
    print(bw_command)
    os.system(bw_command) # run command

    if (show):
        im = image.imread(in_path) # load image as pixel array
        im2 = image.imread(out_path) # load image as pixel array
        fig, axs = pyplot.subplots(1, 2)  # Create figure for 2 plots
        axs[0].imshow(im)  # Show first image
        axs[0].set_title("Original")
        axs[1].imshow(im2)  # Show second image
        axs[1].set_title("B&W")
        pyplot.show()

    return