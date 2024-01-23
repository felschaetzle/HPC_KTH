import psutil
import time
import matplotlib.pyplot as plt
import threading

class CPUMonitor:
    def __init__(self, duration, interval):
        self.duration = duration
        self.interval = interval
        self.cpu_data = {i: [] for i in range(psutil.cpu_count())}
        self.lock = threading.Lock()

    def monitor_cpu_usage(self):
        # Monitor CPU usage
        start_time = time.time()
        while time.time() - start_time < self.duration:
            with self.lock:
                cpu_percents = psutil.cpu_percent(interval=self.interval, percpu=True)
            for i, percent in enumerate(cpu_percents):
                self.cpu_data[i].append(percent)
            time.sleep(self.interval)

    def start(self):
        self.thread = threading.Thread(target=self.monitor_cpu_usage)
        self.thread.start()

    def plot(self):
        # Wait for the monitoring thread to finish
        self.thread.join()

        # Plot CPU usage
        for i, data in self.cpu_data.items():
            plt.plot(data, label=f'CPU {i}')
        plt.xlabel('Time (s)')
        plt.ylabel('CPU Usage (%)')
        plt.legend()
        plt.show()

        # Print summary table
        for i, data in self.cpu_data.items():
            print(f'CPU {i}: Max Usage = {max(data)}%, Avg Usage = {sum(data)/len(data)}%')

# Monitor CPU usage for 20 seconds, updating every second
monitor = CPUMonitor(20, 1)
monitor.start()

# Run your code here

# Plot the results
monitor.plot()