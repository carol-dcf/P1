def rgb2yuv(rgb):
    """
    Translator from RGB to YUV
    :param: rbg: 3 value list containing color information in RGB space
    :return: yuv: 3 value list containing color information in YUV space
    """
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    y = 0.257*r + 0.504*g + 0.098*b + 16
    u = -0.148*r - 0.291*g + 0.439*b + 128
    v = 0.439*r - 0.368*g - 0.071*b + 128
    yuv = [y, u, v]
    return yuv

def yuv2rgb(yuv):
    """
    Translator from YUV to RGB
    :param: yuv: 3 value list containing color information in YUV space
    :return: rbg: 3 value list containing color information in RGB space
    """
    y = yuv[0]
    u = yuv[1]
    v = yuv[2]
    r = 1.164 * (y - 16) + 1.596 * (v - 128)
    g = 1.164 * (y - 16) - 0.813 * (v - 128) - 0.391 * (u - 128)
    b = 1.164 * (y - 16) + 2.018 * (u - 128)
    rgb = [r, g, b]
    return rgb