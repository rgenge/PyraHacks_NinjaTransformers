from ultralytics import YOLO
import torch
import torchvision
import cv2
import numpy as np
import time
import os

def main():
    #setup yolov8 model
    YOLO_VERBOSE=False
    model = YOLO("yolov8n-seg.pt")
    
    #setup image
    webcam = cv2.VideoCapture(0)
    ret, frame = webcam.read()
    while not ret:
        ret, frame = webcam.read()


    count=0
    shape_index=0

    #setup images
    shapes_images=os.listdir("shapes")
    shape=shapes_images[shape_index]
    shape_frame=cv2.imread("shapes/"+shape)

    #setup time variables
    t_loop=time.time()
    t_print=time.time()
    t_switch=time.time()
    while cv2.waitKey(1) < 0:
        #get shape
        if time.time()-t_switch>3:
            sum_base=np.sum(human_mask)
            sum_overlap=np.sum(human_mask*shape_frame[:,:,0])/255
            print("Difference %: ",100*sum_overlap/sum_base)

            t_switch=time.time()
            shape_index+=1
            if shape_index>=len(shapes_images):
                shape_index=0
            shape=shapes_images[shape_index]
            shape_frame=cv2.imread("shapes/"+shape)

        

        #record shapes and print
        count+=1
        if time.time()-t_print>1:
            t_print=time.time()
            cv2.imwrite("shapes_record/shapes"+str(count)+".jpg",blank)
        t_loop=time.time()

        #get frames
        ret, frame = webcam.read()
        frame = cv2.flip(frame, 1)
        if not ret:
            break

        #segment image
        results = model(frame,verbose=YOLO_VERBOSE)
        human_mask=np.array(results[0].masks[0].data[0].cpu())
        frame=cv2.resize(frame,(human_mask.shape[1],human_mask.shape[0]))
        frame[:,:,0]=frame[:,:,0]*human_mask
        frame[:,:,1]=frame[:,:,1]*human_mask
        frame[:,:,2]=frame[:,:,2]*human_mask

        #create blank image
        blank=np.zeros((frame.shape[0],frame.shape[1],3))
        blank[:,:,0]=human_mask*255
        blank[:,:,1]=human_mask*255
        blank[:,:,2]=human_mask*255

        blue=np.zeros((frame.shape[0],frame.shape[1],3))
        blue[:,:,2]=human_mask*255

        #make game frame
        


        #Blue overlay
        game_frame=np.zeros((frame.shape[0],frame.shape[1],3))
        game_frame[:,:,1]=human_mask*255
        #game_frame[:,:,1]=frame[:,:,1]+game_frame[:,:,1]
        game_frame[:,:,2]=shape_frame[:,:,0]


        #Human overlay
        # game_frame=np.copy(shape_frame)
        # game_frame[:,:,0]=frame[:,:,0]+game_frame[:,:,0]
        # game_frame[:,:,1]=frame[:,:,1]+game_frame[:,:,1]
        # game_frame[:,:,2]=frame[:,:,2]+game_frame[:,:,2]

        
        #show frame
        cv2.imshow('YOLOv8', game_frame)

if __name__ == '__main__':
    main()