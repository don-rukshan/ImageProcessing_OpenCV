import numpy as np
import cv2

def increase_brightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result


image = cv2.imread("Lenna.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("original image", image)
#for y in range(1,image.shape[0]):
    #for x in range(1,image.shape[1]):

        #Invert Image
        #image[y,x] = 255 - image[y,x];

        #Brightness Change
        #i = image[y,x]+100;
        #image[y,x] = i if i<256 else 255

        #flip image
#for y in range(0, image.shape[0]):
    #for x in range(1,int(image.shape[1]/2)):
       # i = image[y, image.shape[1]-x]
        #image[y,image.shape[1]-x] = image[y,x]
        #image[y,x]=i

        # contrast image
#for y in range(0,image.shape[0]):
    #for x in range(1,int(image.shape[1]/2)):
       # image[y,x,0] = (255,255,255)-image[y,x,0]

       #Binary Image
#for y in range (0,image.shape[0]):
    #for x in range(1,int(image.shape[1])):
        #image[y,x] = 0 if image[y,x]<180 else 255

        # Detect horizontal edges
for y in range (0, image.shape[0]-1):
    for x in range(1,int(image.shape[1]-1)):
        i = int(image[y,x]) - int (image[y,x+1])
        image[y,x] = i*4 if i >0 else 0




cv2.imshow("Modified Image", image)
cv2.waitKey(0)



#brightness_function = increase_brightness(image, 20)
