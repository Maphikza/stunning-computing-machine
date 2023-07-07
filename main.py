from PIL import Image

# Open the PNG image
image = Image.open('modified_image.png')

# Resize the image to 192x192 pixels
icon_192 = image.resize((192, 192), resample=Image.LANCZOS)

# Resize the image to 512x512 pixels
icon_512 = image.resize((512, 512), resample=Image.LANCZOS)

# Save the resized images as PNG files
icon_192.save('icon_192.png', format='PNG')
icon_512.save('icon_512.png', format='PNG')

