from PIL import Image
import matplotlib.pyplot as plt
# Open the image file
image = Image.open('path/to/image.jpg')  # Replace with the path to your image file

# Display the image
plt.imshow(image)
plt.axis('off')  # Remove axis ticks and labels
plt.show()