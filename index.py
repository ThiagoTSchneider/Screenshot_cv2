import socket
import threading
import subprocess
import os
import time
import cv2 as cv
import numpy as np
import pyautogui
#-------------------------ON_SPIRIT-----------------------------#

def screenshot():
    while True:
        img = pyautogui.screenshot()
        img = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
        cv.imwrite("screenshot.png", img)
        time.sleep(1)

screenshot()
