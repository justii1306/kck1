import cv2
import numpy as np


def getXY(point: list):
    return point[0]

# Wczytanie obrazu
image = cv2.imread('image.png', cv2.COLOR_BGR2GRAY)
cv2.imshow('Wczytany obraz', image)

# Znalezienie konturów w zdjęciu i zaznaczenie ich na kopii obrazu
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)      # wyszarzenie obrazu
gray = cv2.erode(gray, None, iterations=2)
gray = cv2.dilate(gray, None, iterations=2)
edged = cv2.Canny(gray, 90, 200)                    # Znalezienie wszystkich konturów (nie wiem co oznaczają wartości 30 i 300
cv2.imshow('Znalezione linie', edged)

# Znalezienie punktów odpowiadających konturom
(_, cnts, _) = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

screenCnt = None

# Przejście po 10 największych konturach
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.01 * peri, True)

    # Jeśli kontur ma cztery punkty, to prawdopodobnie znaleziono obraz
    if len(approx) == 4:
        screenCnt = approx
        break

cv2.drawContours(image, [screenCnt], -1, (0, 233, 0), 3)
cv2.imshow('Znaleziony obraz', image)
cv2.waitKey()
