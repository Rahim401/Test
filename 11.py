import cv2
import matplotlib.pyplot as plt
import numpy as np
# Read the image
image = cv2.imread("original_image.jpg")
# Convert the image to grayscale (contours work best on binary images)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Apply thresholding (you can use other techniques like Sobel edges)
__,binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# Find contours
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Draw all contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
# Display the result
plt.imshow(gray)
cv2.imwrite("gray.png",gray)
plt.imshow(binary_image)
cv2.imwrite("binary_image.png",binary_image)
plt.imshow(image)
cv2.imwrite("image.png",image)
plt.imshow(contours)
cv2.imwrite("Red.png",contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
