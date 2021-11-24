# P1
## P1 of SCAV subject
In this project you can see applied some **basic** functionalities of the ffmpeg software into the images, as well as some applied theory concepts on JPEG. All the functions can be applied to any other image if the input_path is changed in the *main.py* file.

To run the program, run the *main.py* and a fully interactive menu will appear. There, you can navigate trough the different proposed exercises.

Instructions are reaaly clear once you are running the files, however, here's a quick guide on how to use it.

| Num | Title         | Short explanation of the function                                                                                                                |
|-----|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | RGB 2 YUV     | Given an input of 3 numbers (in RGB), it converts it to YUV space, and then back to RGB |
| 2   | Resize Image | Given an input file, downscale the image by a given factor (e.g. 2 means that the new size will be half the original). You can choose to visualize the results. |
| 3   | Image 2 BW  | Given an input file, convert it to grayscale and compress it (you can see that since the new image is in B&W, you will not appreciate the difference). You can choose to visualize the results. |
| 4   | Run Length  | Given an input sequence, encode it using the run-length algorithm. |
| 5   | DCT  | Given a list (especified through the command line), compute the DCT coefficients, and then convert it back to the original values. |
| 0   | Exit          | Close application. |

(All the files generated in the different exercises on the image can be seen in the Results folder)

These functions have some library dependencies, if you do not have them installed in your device, run the *dependencies.py* file.
