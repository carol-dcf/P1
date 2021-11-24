import os
# load and display an image with Matplotlib
from matplotlib import pyplot
from matplotlib import image

def resize(in_path, down_scale, show):
    """
    Downscale an image
    :param in_path: (str) path of input image
    :param down_scale: (int) factor of downscaling: 2, 4...
    :param show: (bool) visualize results
    :return:
    """
    # load image as pixel array
    im = image.imread(in_path)
    print("Original Shape: ", im.shape)
    out_path = "resized_" + in_path # Output path
    resize_command = "ffmpeg -i " + in_path + " -vf " + "\"scale = " + str(
        im.shape[1]//down_scale) + ":" + str(im.shape[0]//down_scale) + "\" " + out_path
    print(resize_command) # FFMPEG command to resize an image to a given scale
    os.system(resize_command) # run command
    # load image as pixel array
    im2 = image.imread(out_path)
    print("New shape: ", im2.shape)

    if (show):
        fig, axs = pyplot.subplots(1, 2) # Create figure for 2 plots
        axs[0].imshow(im) # Show first image
        axs[0].set_title("Original")
        axs[1].imshow(im2) # Show second image
        axs[1].set_title("Downscaled")
        pyplot.show()

    return
