import matplotlib.pyplot as plt
from PIL import Image

image_file = Image.open("User,Esquirio/Python/Python.png")

imgplot = plt.imshow(image_file)
plt.show ()

image_file = image_file.convert('L')

imgplot = plt.imshow(image_file)
plt.show ()