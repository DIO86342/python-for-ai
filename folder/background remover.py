from rembg import remove
from PIL import Image

input_path = 'story - Copy.jpg'
output_path = 'story_no_bg.png'

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)
output_image.show()