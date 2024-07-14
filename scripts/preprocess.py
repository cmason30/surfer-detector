import cv2
import numpy as np


def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply median filter to reduce noise while preserving edges
    median_filtered = cv2.medianBlur(gray, 3)

    # Enhance contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(20, 20))
    enhanced = clahe.apply(median_filtered)

    return enhanced


def adaptive_threshold_image(filtered, method=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, block_size=3, C=2):
    # Apply adaptive thresholding to highlight the darkest objects
    thresh = cv2.adaptiveThreshold(
        filtered,
        255,
        method,
        cv2.THRESH_BINARY_INV,
        block_size,
        C
    )

    return thresh


image = cv2.imread('capture3_2024-06-22 18:05:57.jpg')
proc_img = preprocess_image(image)
proc2_img = adaptive_threshold_image(proc_img)

cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', proc2_img)

cv2.waitKey(0)

    # Destroy all OpenCV windows
cv2.destroyAllWindows()