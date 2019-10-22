#import statements
import cv2, argparse, numpy

#create an argument parser for the program
parser = argparse.ArgumentParser()
parser.add_argument('--input-image-path', '-i', dest = 'inputImage', required = True)
parser.add_argument('--output-image-path', '-o', dest = 'outputImage', required = True)
parser.add_argument('--grayscale-color-threshold', '-t', dest = 'colorThreshold', required = True)

#parse the arguments
arguments = parser.parse_args()

#open the image using opencv
imageUnedited = cv2.imread(str(arguments.inputImage))

#sharpen the image using things i dont understand
kernel = numpy.array([[0, -1, 0], 
                      [-1, 5,-1], 
                      [0, -1, 0]])
imageSharpened = cv2.filter2D(imageUnedited, -1, kernel)

#convert the image to a grayscale image
imageGrayscale = cv2.cvtColor(imageSharpened, cv2.COLOR_BGR2GRAY)

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