from rembg import remove
from PIL import Image

input_path = 'assets/images/new-logo.png'
output_path = 'assets/images/new-logo-transparent.png'

print("Removing background from the new logo...")
input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)
print("Background removed and saved successfully.")
