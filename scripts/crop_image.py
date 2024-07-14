import cv2

# Load the image
image = cv2.imread('capture3.jpg')

# Check if the image is loaded successfully
if image is None:
    print("Error: Could not load image.")
else:
    # Get the dimensions of the image
    height, width, channels = image.shape
    print(f"Image dimensions: Width = {width}, Height = {height}, Channels = {channels}")

    # Define the coordinates for the rectangle starting from the bottom-left corner
    top_left = (0, height - 825)       # (x, y) coordinates for the top-left corner
    bottom_right = (1090, height)      # (x, y) coordinates for the bottom-right corner

    # Ensure the coordinates are within the image dimensions
    top_left = (max(0, top_left[0]), max(0, top_left[1]))
    bottom_right = (min(width, bottom_right[0]), min(height, bottom_right[1]))

    # Draw the rectangle on the original image
    outlined_image = image.copy()
    cv2.rectangle(outlined_image, top_left, bottom_right, (0, 255, 0), 2)

    # Crop the image using the coordinates
    roi = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

    # Display the original image, outlined image, and the cropped region
    cv2.imshow('Original Image', image)
    cv2.imshow('Outlined Image', outlined_image)
    cv2.imshow('Cropped ROI', roi)

    # Save the outlined image and cropped region
    cv2.imwrite('outlined_image.jpg', outlined_image)
    cv2.imwrite('cropped_roi.jpg', roi)
    print("Outlined image saved as 'outlined_image.jpg'")
    print("Cropped ROI saved as 'cropped_roi.jpg'")

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Destroy all OpenCV windows
    cv2.destroyAllWindows()