# Done by Frannecklp

import cv2
import numpy as np
import time
import pyscreenshot

def grab_screen(region=None):

    last_time = time.time()
    bbox = region if region is not None else (0,40,800,640)
    # part of the screen
    screenshot=cv2.cvtColor(np.array(pyscreenshot.grab(bbox=bbox)), cv2.COLOR_BGRA2RGB)
    # print('loop took {} seconds'.format(time.time()-last_time))
    return screenshot
