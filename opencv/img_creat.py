import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create a blank black image
img = np.zeros((500, 500), dtype=np.uint8)

# Draw some white shapes (circle, square, triangle)
cv2.circle(img, (150, 150), 50, (255), -1)  # Circle
cv2.rectangle(img, (300, 50), (400, 150), (255), -1)  # Square
pts = np.array([[250, 300], [300, 400], [200, 400]], np.int32)  # Triangle
cv2.fillPoly(img, [pts], (255))

# Add some random noise
for _ in range(100):
    x, y = np.random.randint(0, 500, 2)
    img[y, x] = 255

# Display the generated image
plt.title('Generated Binary Image with Shapes and Noise')
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()

# Save the image if needed
cv2.imwrite('binary_image_with_shapes.png', img)
