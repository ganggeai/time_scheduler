# -*- coding: utf-8 -*-

import schedule as timer
import time
def task1():
    print('excuteing stask1 at :{0}'.format(time.ctime()))
    time.sleep(3)
    print('stask1 finished')
timer.every(1).minute.do(task1)

def start_timer():
    while True:
        timer.run_pending()
        time.sleep(1)


