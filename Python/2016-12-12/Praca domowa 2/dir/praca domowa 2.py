import cv2
import numpy as np


def getXY(point: list):
    return point[0]

# Wczytanie obrazu
image = cv2.imread('image.png', cv2.COLOR_BGR2GRAY)
cv2.imshow('Wczytany obraz', image)

# Znalezienie konturów w zdjęciu i zaznaczenie ich na kopii obrazu
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)      # wyszarzenie obrazu
gray = cv2.bilateralFilter(gray, 11, 17, 17)        # Blur obrazu
edged = cv2.Canny(gray, 30, 300)                    # Znalezienie wszystkich konturów (nie wiem co oznaczają wartości 30 i 300
cv2.imshow('Znalezione linie', edged)

# Znalezienie punktów odpowiadających konturom
(_, cnts, hir) = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cnts = sorted(cnts, key = cv2.contourArea, reverse = True)

# cnts = [i for i in cnts if is_line(i)]

# screenCnt = None

# Przejście po 10 największych konturach
# for c in cnts:
#     peri = cv2.arcLength(c, True)
#     approx = cv2.approxPolyDP(c, 0.02 * peri, True)
#
#     # Jeśli kontur ma cztery punkty, to prawdopodobnie znaleziono obraz
#     if len(approx) == 4:
#         screenCnt = approx
#         break
# for i in cnts:

# for i in range(len(cnts)):
#     peri = cv2.arcLength(cnts[i], False)
#     cv2.drawContours(image, cv2.approxPolyDP(cnts[i], 0.02 * peri, False), -1, (0, 255, 0), 3)
#     cv2.imshow('Znaleziony obraz', image)
#     cv2.waitKey(300)


# for i in range(len(cnts)):
#     print(hir[0][i][3] < 0)
#
#     if hir[0][i][3] < 0:
#         outCnts.append(cnts[i])
#     else:
#         print("txt, ")

# cv2.drawContours(image, cnts, -1, (0, 255, 0), 3)
# print(largeCnt)
# print(largeCntArea)

imageArea = 0
imageCnt = [[0,0], [1,0], [0,1], [1,1]]

for cnt in cnts:
    for point in cnt:
        xy = getXY(point)
        if topLeft is None:
            topLeft = xy
            topRight = xy
            bottomLeft = xy
            bottomRight = xy
            continue

        if (xy[0] <= topLeft[0] & xy[1] <= topLeft[1]) | ():
            topLeft = xy
            continue

        if xy[0] >= topRight[0] & xy[1] <= topRight[1]:
            topRight = xy
            continue

        if xy[0] <= bottomLeft[0] & xy[1] >= bottomLeft[1]:
            bottomLeft = xy
            continue

        if xy[0] >= bottomRight[0] & xy[1] >= bottomRight[1]:
            bottomRight = xy
            continue

print(topLeft)
print(topRight)
print(bottomLeft)
print(bottomRight)
imageCnt = np.array([[topLeft], [topRight], [bottomLeft], [bottomRight]])

cv2.drawContours(image, cnts, -1, (0, 255, 0), 3)
cv2.polylines(image, imageCnt, True, (0, 0, 255), 10)
# cv2.drawContours(image, largeCnt, -1, (255, 0, 0), 5)
cv2.imshow('Znaleziony obraz', image)
cv2.waitKey()
