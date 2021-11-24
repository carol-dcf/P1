# Necessary imports
import rgb_yuv as ry
import resize_im as ri
import black_and_white as bw
import runlength as rl
import dct_converter as dc

if __name__ == "__main__":
    # Interactive menu
    ex = 1
    while ( ex != 0 ):
        print("\033[1m\nChoose an exercise:\033[0m")
        print("\t 1. RGB 2 YUV" + "\n\t 2. Resize Image" + "\n\t 3. Image 2 BW"+ "\n\t 4. Run Length" + "\n\t 5. DCT" + "\n\t 0. Exit")

        ex = int(input())

        #### 1 #####
        if (ex == 1):
            print("\033[1mEXERCISE 1\033[0m")
            print("Enter RGB values one by one: ")
            rgb = []
            for i in range(0,3):
                rgb.append(int(input()))

            yuv = ry.rgb2yuv(rgb)
            print("Value in YUV space", yuv)
            print("Inverse operation:\nValue in RGB space", ry.yuv2rgb(yuv))

        #### 2 #####
        elif (ex == 2):
            print("\n\033[1mEXERCISE 2\033[0m")
            down_scale = int(input("Factor of downscaling: "))
            show = bool(int(input("Visualize Images (True = 1 / False = 0): ")))
            ri.resize("102286_gallery.jpg", down_scale, show)

        elif (ex == 3):
            #### 3 #####
            print("\n\033[1mEXERCISE 3\033[0m")
            show = bool(int(input("Visualize Images (True = 1 / False = 0): ")))
            bw.bw_im("102286_gallery.jpg", show)

        elif (ex == 4):
            #### 4 #####
            print("\n\033[1mEXERCISE 4\033[0m")
            input_sequence = str(input("Sequence to encode: "))
            output_sequence = rl.encode(input_sequence)
            print("Encoded sequence:  ", output_sequence)

        elif (ex == 5):
            print("\n\033[1mEXERCISE 5\033[0m")
            input_list = input("List of numbers separated by a coma and a space: ").strip("][").split(", ")
            input_list = list(map(int, input_list))
            print(input_list)
            output_dct = dc.dct1d(input_list)
            print(output_dct)
            output_idct = dc.idct1d(output_dct)
            print(output_idct)

        elif (ex == 0):
            print("Application closed.")
        else:
            print("Not a valid option.")