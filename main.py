import numpy as np
import cv2

#Ref setup for variables used in cv resize function
stock_image = cv2.imread("brheart.png", )
print('Original Dimensions : ', stock_image.shape)
scale_percent = 25  # percent of original size
width = int(stock_image.shape[1] * scale_percent / 100)
height = int(stock_image.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize the image
resized = cv2.resize(stock_image, dim, interpolation=cv2.INTER_AREA)
print('Resized Dimensions : ', resized.shape)
rgb_img = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB) #Convert from BGR format to RGB
cv2.imshow("Resized image", resized)
cv2.waitKey(100)


rgb_img [np.all(rgb_img == (0, 255, 0), axis=-1)] = (255,255,255)
cv2.imshow("Resized image", rgb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Check to see if the BGR to RGB had worked
# px = rgb_img [:2, :2]
# print(px)

