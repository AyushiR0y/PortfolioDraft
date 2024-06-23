import cv2

# Path to the image
image_path = r'C:\Users\ayush\Documents\codes\portfolio\.vscode\dip\input_image.jpg'

# Read the image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not open or find the image.")
    exit()

# Apply contrast adjustment (for example, using CLAHE)
# Create a CLAHE object (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

# Convert image to LAB color space
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Split LAB image into L, A, and B channels
l_channel, a_channel, b_channel = cv2.split(lab_image)

# Apply CLAHE to the L channel
l_channel_eq = clahe.apply(l_channel)

# Merge the CLAHE enhanced L channel with the original A and B channels
lab_image_eq = cv2.merge((l_channel_eq, a_channel, b_channel))

# Convert LAB image back to BGR color space
adjusted_image = cv2.cvtColor(lab_image_eq, cv2.COLOR_LAB2BGR)

# Write the adjusted image to a file
output_image_path = r'C:\Users\ayush\Documents\codes\portfolio\.vscode\dip\adjusted_image.jpg'
cv2.imwrite(output_image_path, adjusted_image)

# Display the adjusted image
cv2.imshow('Adjusted Image', adjusted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
