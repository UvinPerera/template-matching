import cv2 as cv
import numpy as np

image = cv.imread('sinhala-text.png') # read image
image_to_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) # convret the readed image to grey
temp = cv.imread('template.png',0) # read the template
width, height = temp.shape[::-1]  # get width and height of the template

result = cv.matchTemplate(image_to_gray,temp,cv.TM_CCOEFF_NORMED) # match template and assign the the result to variable
threshold = 0.9  # set filtering thresholds
loc = np.where( result >= threshold)

num_of_occurences =0 # number of occurences
for pt in zip(*loc[::-1]):
    cv.rectangle(image, pt, (pt[0] + width, pt[1] + height), (0,255,0), 2) # draw rectangles in the indentified regions
    num_of_occurences=num_of_occurences+1 # increment the number ofoccurences
    
cv.imwrite('result.png',image) # Save the image after highliting the regions
print("Number of Occurences:"+str(num_of_occurences)) # print the number of occurences