# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:55:31 2021

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

from watch_folder import *


from video_processing import video_process 

from config import *




def read_video(rotate,greyscale,savefile):
    process = []
    for filename in os.listdir('.\Data'):
         process.append(multiprocessing.Process(target=video_process,args=(filename,rotate,greyscale,savefile)))
    
    return process



if __name__ == "__main__":

    
    
    logger = setup_logging()
    logger.info('Logging setup finished',         extra={'file_id':'info.log'})


    parser = argparse.ArgumentParser()

    parser.add_argument('-r', action='store_true')
    parser.add_argument('-g', action='store_true')
    parser.add_argument('-s', action='store_true')

    args = parser.parse_args()
    
    rotate = args.r
    greyscale = args.g
    savefile = args.s
    
    
    process = read_video(rotate, greyscale, savefile)
    
    
    for _ in process:
        _.start()
        
    start_event(rotate, greyscale, savefile)
    

    
    print("Both processes finished execution!") 
  
    # check if processes are alive 
    #print("Process p1 is alive: {}".format(procs1.is_alive())) 
    #print("Process p2 is alive: {}".format(procs2.is_alive())) 


    
    
    
    
    