# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 18:17:32 2021

@author: Dalindalz
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 19:05:29 2021

@author: Dalindalz
"""
import cv2
import tqdm
import time 
import logging

from config import *

VIDEO_PATH = 'C:/Detect/Data/'






def video_process(video_name,rotate , greyScale , saveFile):
    video = cv2.VideoCapture(VIDEO_PATH+video_name)
    if rotate:
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    elif not rotate:
        height = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        width = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    frames_per_second = video.get(cv2.CAP_PROP_FPS)
    num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    if greyScale:
        video_writer = cv2.VideoWriter(video_name,fourcc, 15.0, (int(height),int(width)),isColor=False)
    elif not greyScale:
        video_writer = cv2.VideoWriter(video_name,fourcc, 15.0, (int(height),int(width)),isColor=True)

    if saveFile:
    
        # Enumerate the frames of the video
        for visualization in tqdm.tqdm(runOnVideo(video, num_frames,rotate, greyScale), total=num_frames):
    
            # Write to video file
            video_writer.write(visualization)
        
    video.release()
    video_writer.release()
    cv2.destroyAllWindows()
    return
    
def runOnVideo(video,maxFrames,rotate, grayScale):
    
    readFrames = 0
    # used to record the time when we processed last frame 
    prev_frame_time = 0
  
    # used to record the time at which we processed current frame 
    new_frame_time = 0


    while True:
        hasFrame, frame = video.read()
        if not hasFrame:
            break
        if rotate:
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE) 

        if grayScale:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       
        new_frame_time = time.time() 
        fps = 1/(new_frame_time-prev_frame_time) 
        prev_frame_time = new_frame_time 
        fps = str(fps)
        
        logger = logging.getLogger('request_logger')
        logger.info('FPS : ' + fps,         extra={'file_id':'info.log'})
        
        yield frame

        readFrames += 1
        if readFrames > maxFrames:
            break
        




