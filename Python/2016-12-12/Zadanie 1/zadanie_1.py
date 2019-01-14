import cv2
import os
import sys
import webbrowser
from PIL import Image

# Get user supplied values
imagePath = "polska_dr_pil.jpg"
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
imageFile = Image.open(imagePath)
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

i = 1
# Creates a directory
try:
    os.stat('image')
except:
    os.mkdir('image')

# Begin creates a html file
html = open('index.html', 'w')

html.write('''<html>
    <head>
        <title>Polscy pilkarze</title>
    </head>
    <body>
''')
    
# Draw a rectangle around the faces, save the images contains faces and add to html code
for (x, y, w, h) in faces:
    imageFile.crop((x, y, x+w, y+h)).resize((128,128)).save('image/' + str(i) + '.jpg')
    html.write('        <img src="image/' + str(i) + '.jpg">\n')
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    i=i+1

html.write('''    </body>
</html>''')
html.close()

cv2.imshow("Faces found", image)
cv2.waitKey(0)

webbrowser.open_new_tab('file:///' + os.path.abspath('index.html'))
