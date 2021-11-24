from scipy.fftpack import dct, idct
import numpy as np
import cv2
import matplotlib.pylab as plt

def dct1d(input_list):
    """
        Function that applies the DCT to a list of numbers
        :param input_list: list of numbers that the DCT will be applied to
        :return: []: list of the dct coefficients
        """
    return dct(np.array(input_list), norm = 'ortho')

def idct1d(input_list):
    """
        Function that applies the inverse DCT to a list of numbers
        :param input_list: coefficients of DCT
        :return: []: list of numbers
        """
    idct_list = idct(np.array(input_list), norm='ortho').tolist()
    return [round(num, 3) for num in idct_list]


def dct2d(input_im):
    # read RGB image and convert to grayscale
    im = cv2.imread(input_im)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    dct_coeff = dct(dct(gray.T, norm = 'ortho').T, norm = 'ortho')
    return dct_coeff


def idct2d(input_im):
    return idct(idct(input_im, norm = 'ortho').T, norm = 'ortho')

