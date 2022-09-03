from PIL import ImageGrab
import time
while True:
    start_time = time.time()

    #screenshot = ImageGrab.grab(bbox=(0, 400, 880, 1950)) #portrait
    screenshot = ImageGrab.grab(bbox=(0, 250, 2600, 1610))
    screenshot = screenshot.convert("RGB")
    screenshot.save("latest.jpg", "jpeg")
    print("Screenshot taken")

    end_time = time.time()
    time_between_shots = end_time - start_time
    print("Time between screenshots: " + str(time_between_shots))

    #time.sleep(1)

