
from PIL import Image

img = Image.open('assets/images/new-logo.png').convert('RGBA')
width, height = img.size

# Check corner pixels to guess background color
corners = [
    img.getpixel((0, 0)),
    img.getpixel((width - 1, 0)),
    img.getpixel((0, height - 1)),
    img.getpixel((width - 1, height - 1))
]
print(f'Corner pixels: {corners}')

