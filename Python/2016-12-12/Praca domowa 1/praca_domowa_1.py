from PIL import Image
from random import shuffle

# Change RGB to RGB, RBG, GRB,
def change_colors(image):
    size = image.size
    colors = [0, 1, 2]
    shuffle(colors)

    for j in range(size[1]):
        for i in range(size[0]):
            xy = (i, j)
            oldPixel = image.getpixel(xy)
            image.putpixel(xy, (oldPixel[colors[0]], oldPixel[colors[1]], oldPixel[colors[2]]))

    return image


# Get user supplied value
imagePath = "obraz.jpg"

# Read the image
image = Image.open(imagePath)

# Get information about count of segments in picture
parts = int(input('Podaj liczbę segmentów w pliku: '))

# Generate information about size of new picture
width, height = image.size
size = min(width, height)
size -= size % parts

# Cut the image
image = image.crop((0, 0, size, size))

if size <= 0:
    print("Ilość segmentów jest większa od wielkości pliku")
    exit(1)

# Generate information about size of part of picture
partSize = size / parts

for j in range(parts):          # multiplier Y
    for i in range(parts):      # multiplier X
        part = (int(i * partSize), int(j * partSize), int((i+1) * partSize), int((j+1) * partSize))
        imagePart = change_colors(image.crop(part))
        image.paste(imagePart, part)

image.save('wynik.jpg', 'JPEG')
