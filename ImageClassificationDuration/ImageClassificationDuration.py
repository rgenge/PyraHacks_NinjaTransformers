from ultralytics import YOLO
import torch
import numpy as np
import time
import tkinter as tk
from threading import Thread
import subprocess
import re

class App:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(text="Press the button to start benchmarking")
        self.label.pack()
        self.button = tk.Button(text="Start", command=self.start_benchmark_thread)
        self.button.pack()
        self.text_area = tk.Text(root, height=32, width=90)
        self.text_area.pack()

        #set size of window
        self.root.geometry("800x600")

        # load model
        self.model = YOLO("yolov8n-seg.pt")

        self.fps_averages = []
        self.fps = 0
        self.count = 0

    def get_gpu_info(self):
        smi_output = subprocess.check_output(['nvidia-smi']).decode('utf-8')
        lines = smi_output.split('\n')
        temperature_line = lines[9]  # GPU temp info is on the 9th line (0-indexed)
        power_line = lines[9]        # Power info is also on the 9th line
        memory_line = lines[9]       # Memory info is on the 10th line

        temperature_match = re.search(r'\d+C', temperature_line)
        power_match = re.search(r'\d+W', power_line)
        memory_match = re.search(r'\d+MiB', memory_line)

        temperature = temperature_match.group() if temperature_match else 'Unknown'
        power = power_match.group() if power_match else 'Unknown'
        memory = memory_match.group() if memory_match else 'Unknown'
        
        return temperature, power, memory

    def start_benchmark_thread(self):
        # Create and start a new thread for the benchmark
        thread = Thread(target=self.run_benchmark)
        thread.start()

    def run_benchmark(self):
        print("Starting")
        t_start = time.time()
        t_interval = time.time()
        while(time.time()<(t_start+300)):
            t_pre_inference = time.time()
            frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
            result = self.model(frame, verbose=False)
            self.count += 1
            self.fps += 1/(time.time() - t_pre_inference)
            if (time.time() - t_interval) > 5:
                self.fps_averages.append(self.fps / self.count)
                gpu_info=self.get_gpu_info()
                gpu_temp=gpu_info[0]
                gpu_power=gpu_info[1]
                gpu_memory=gpu_info[2]
                self.text_area.insert(tk.END, f"FPS for 640x480: {self.fps / self.count} GPU temp: {gpu_temp},GPU power: {gpu_power}, GPU memory: {gpu_memory}\n")
                #self.text_area.insert(tk.END, f"GPU info: {self.get_gpu_info()}\n")
                self.root.update()
                self.fps = 0
                self.count = 0
                t_interval = time.time()

root = tk.Tk()
app = App(root)
root.mainloop()
