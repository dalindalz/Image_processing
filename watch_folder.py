# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:19:11 2021

@author: Dalindalz
"""

import os
import multiprocessing 
import argparse
import sys
import time

from multiprocessing import *

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


from video_processing import video_process 

from config import *


RORATE_FLAG = True
GRAY_FLAG = True
SAVE_FLAG = True


def countdown(t,my_observer): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    my_observer.stop()
    my_observer.join()
    print("Event Stopped")
    
    sys.exit()


def start_event(rotate,greyscale,savefile):
    
    RORATE_FLAG = rotate
    GRAY_FLAG = greyscale
    SAVE_FLAG = savefile
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created

    path = ".\Data"
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    
    my_observer.start()
    countdown(600,my_observer)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()

def on_created(event):
    logger = logging.getLogger('request_logger')
    logger.info('New File created : ' + str(os.path.basename(event.src_path) ), extra={'file_id':'info.log'})
    p1 = multiprocessing.Process(target=video_process,args=(os.path.basename(event.src_path),RORATE_FLAG,GRAY_FLAG,SAVE_FLAG))
    p1.start()
