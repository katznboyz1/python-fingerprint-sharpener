#import statements
import cv2, argparse

#create an argument parser for the program
parser = argparse.ArgumentParser()
parser.add_argument('--input-image-path', '-i', dest = 'inputImage', required = True)
parser.add_argument('--output-image-path', '-o', dest = 'outputImage', required = True)
parser.add_argument('--grayscale-color-threshold', '-t', dest = 'colorThreshold', required = True)

#parse the arguments
arguments = parser.parse_args()

#open the image using opencv
imageUnedited = cv2.imread(str(arguments.inputImage))

#convert the image to a grayscale image
imageGrayscale = cv2.cvtColor(imageUnedited, cv2.COLOR_BGR2GRAY)

#iterate through the image to filter out any colors below the threshold
thresholdGrayscaleInt = int(arguments.colorThreshold)
for YCoord in range(imageGrayscale.shape[0]):
    for XCoord in range(imageGrayscale.shape[1]):
        color = int(imageGrayscale[YCoord, XCoord])
        newColor = 0
        if (color > thresholdGrayscaleInt):
            newColor = 255
        imageGrayscale[YCoord, XCoord] = newColor

#save the image
cv2.imwrite(str(arguments.outputImage), imageGrayscale)