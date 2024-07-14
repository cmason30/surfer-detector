
import cv2
import numpy as np

# Load the image
image = cv2.imread('capture3_2024-06-22 14:37:04.jpg')

# Check if the image is loaded successfully
if image is None:
    print("Error: Could not load image.")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply manual thresholding with a very low threshold value
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

    # Convert the thresholded image back to BGR so it can be blended with the original

    # Blend the original image and the thresholded image

    # Display the original, thresholded, and blended images
    cv2.imshow('Original Image', image)
    cv2.imshow('Thresholded Image', thresh)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Destroy all OpenCV windows
    cv2.destroyAllWindows()
