import psutil
import time
import matplotlib.pyplot as plt
import threading
import pandas as pd
import numpy as np

class CPUMonitor:
    def __init__(self, interval, csv_file_name):
        self.interval = interval
        self.cpu_data = {i: [] for i in range(psutil.cpu_count())}
        # self.lock = threading.Lock()
        self.interval = interval
        self.csv_file_name = csv_file_name

    def monitor_cpu_usage(self):
        # Monitor CPU usage
        # start_time = time.time()
        global running

        running = True

        # currentProcess = psutil.Process()

        # start loop
        while running:
            # while time.time() - start_time < self.duration:
            # with self.lock:
            cpu_percents = psutil.cpu_percent(interval=self.interval, percpu=True)
            print(cpu_percents)
            for i, percent in enumerate(cpu_percents):
                self.cpu_data[i].append(percent)
            time.sleep(self.interval)

    def start(self):
        self.thread = threading.Thread(target=self.monitor_cpu_usage)
        self.thread.start()

    def stop(self):
        global running
        running = False
        self.thread.join()


    def plot(self):
        # Wait for the monitoring thread to finish
        self.thread.join()

        # # Plot CPU usage
        for i, data in self.cpu_data.items():
            plt.plot(data, label=f'CPU {i}')
        plt.xlabel('Time (s)')
        plt.ylabel('CPU Usage (%)')
        plt.legend()
        plt.show()

        # Print summary table
        for i, data in self.cpu_data.items():
            print(f'CPU {i}: Max Usage = {max(data)}%, Avg Usage = {sum(data)/len(data)}%')

        # print(self.cpu_data)
        df = pd.DataFrame(self.cpu_data)
        print(df.columns)
        end_time = len(df[0]) * self.interval
        df["time_stamp"] = np.arange(0,end_time, self.interval)
        df.to_csv(self.csv_file_name, index=False)
        print(df)
# # Monitor CPU usage for 20 seconds, updating every second
# monitor = CPUMonitor(1)
# monitor.start()

# for i in range(5):
#     print(i)
#     time.sleep(1)

# monitor.stop()

# # Run your code here

# # Plot the results
# monitor.plot()