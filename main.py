import pyautogui
from PIL import ImageGrab
from PIL import Image


startTitle = Image.open('./startTitle.png')

# start game
titleLocate = pyautogui.locateOnScreen(
    startTitle, region=(1237, 587, 350, 144), grayscale=True)
x = titleLocate[0] + 50
y = titleLocate[1]
pyautogui.click(x, y)
# pyautogui.displayMousePosition()

Y = int(600)
X1 = int(1280)
X2 = int(1362)
X3 = int(1454)
X4 = int(1543)
SCORE = 0

while 1:
    if ImageGrab.grab().getpixel((X1, Y))[0] == 0:
        pyautogui.click(X1, Y)
        SCORE += 1
        if SCORE == 400:
            Y += 160
        if SCORE == 500:
            Y += 50
        print(SCORE)
        print(X1, Y, 'Tile 1')

    if ImageGrab.grab().getpixel((X2, Y))[0] == 0:
        pyautogui.click(X2, Y)
        SCORE += 1
        if SCORE == 400:
            Y += 160
        if SCORE == 500:
            Y += 50
        print(SCORE)
        print(X2, Y, 'Tile 2')

    if ImageGrab.grab().getpixel((X3, Y))[0] == 0:
        pyautogui.click(X3, Y)
        SCORE += 1
        if SCORE == 400:
            Y += 160
        if SCORE == 500:
            Y += 60
        print(SCORE)
        print(X3, Y, 'Tile 3')

    if ImageGrab.grab().getpixel((X4, Y))[0] == 0:
        pyautogui.click(X4, Y)
        SCORE += 1
        if SCORE == 400:
            Y += 160
        if SCORE == 500:
            Y += 60
        print(SCORE)
        print(X4, Y, 'Tile 4')
