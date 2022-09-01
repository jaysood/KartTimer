from PIL import ImageGrab
import time

enough = False
count = 0
starttime = time.time()

while enough == False:
    screenshot = ImageGrab.grab(bbox=(0, 0, 7000, 7000))
    screenshot.save(str(count) + "temp.png")
    print("Screenshot taken")
    count += 1
    if count == 10:
        enough = True
        sleep(1)

