from ultralytics import YOLO
import torch
import numpy as np
import time
import tkinter as tk
from threading import Thread

class App:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(text="Press the button to start benchmarking")
        self.label.pack()
        self.button = tk.Button(text="Start", command=self.start_benchmark_thread)
        self.button.pack()
        self.text_area = tk.Text(root)
        self.text_area.pack()

        # load model
        self.model = YOLO("yolov8n-seg.pt")
        self.steps = ["144","240","480","720","1080","4k","8k"]
        self.step_resolutions = [(256,144),(320,240),(640,480),(1280,720),(1920,1080),(3840,2160),(7680,4320)]
        self.fps_averages = []
        self.fps = 0
        self.count = 0

    def start_benchmark_thread(self):
        # Create and start a new thread for the benchmark
        thread = Thread(target=self.run_benchmark)
        thread.start()

    def run_benchmark(self):
        # Warmup
        self.text_area.insert(tk.END, "Warming up\n")
        self.root.update()
        t_warmup = time.time()
        frame = np.random.randint(0,255,(480,640,3),dtype=np.uint8)
        while(time.time()<(t_warmup+3)):
            result = self.model(frame, verbose=False)

        # Benchmark
        self.text_area.insert(tk.END, "Starting benchmark\n")
        self.root.update()
        for i in range(len(self.steps)):
            fps = 0
            count = 0
            t_start = time.time()
            frame = np.random.randint(0,255,(self.step_resolutions[i][1], self.step_resolutions[i][0],3),dtype=np.uint8)
            result = self.model(frame,verbose=False)
            while ((time.time()-t_start)<6):
                t_pre_inference = time.time()
                result = self.model(frame,verbose=False)
                if (time.time()-t_start)>4:
                    count+=1
                    fps+=(1/(time.time()-t_pre_inference))
            self.text_area.insert(tk.END, f"FPS for {self.steps[i]}p: {fps/count}\n")
            self.root.update()
            self.fps_averages.append(fps/count)

        # save fps_averages to text file
        with open("fps_averages.txt","w") as f:
            for i in range(len(self.fps_averages)):
                f.write(self.steps[i]+"p: "+str(self.fps_averages[i])+"\n")

root = tk.Tk()
app = App(root)
root.mainloop()