import cv2
image = cv2.imread("C:\\Users\\Shiva Goud\\Pictures\\Screenshots\\chikki.png")
# Display the image using OpenCV
cv2.imshow('woman', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To check dimensions of the image
print(image.shape)