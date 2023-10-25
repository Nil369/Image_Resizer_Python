import cv2

# Configurable Parameters:

source = "akash.png"
destination = 'newImage.jpeg'
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# percent by which the image is resized

# calculate the 50 percent of original dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
cv2.imshow("Resized Image_Quality check", src)
cv2.waitKey(0)

# I will learn django make it use-able for website & other multiple stuffs
