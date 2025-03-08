import tkinter as tk
import subprocess

def cpu_Usage():
	result = subprocess.run(["top", "-bn1"], stdout=subprocess.PIPE, text=True)
	cpu_line = result.stdout.split("\n")[2]
	cpu_idle = float(cpu_line.split(",")[3].strip().replace("%id", "").split()[0])
	cpu_usage = 100 - cpu_idle
	return f"CPU Usage: {cpu_usage:.2f}%"

def memory_Usage():
	result = subprocess.run(["free", "-m"], stdout=subprocess.PIPE, text=True)
	memory_line = result.stdout.split("\n")[1]
	memory_total = float(memory_line.split()[1])
	memory_used = float(memory_line.split()[2])
	memory_percentage = (memory_used / memory_total) * 100
	return f"Memory Usage: {memory_percentage:.2f}%"

def disk_Usage():
	result = subprocess.run(["df", "-h", "/"], stdout=subprocess.PIPE, text=True)
	disk_line = result.stdout.split("\n")[1]
	disk_usage =  disk_line.split()[4]
	return f"Disk Usage: {disk_usage}"

def update_gui():
	cpu_label.config(text=cpu_Usage())
	memory_label.config(text=memory_Usage())
	disk_label.config(text=disk_Usage())

	root.after(5000, update_gui)

root = tk.Tk()
root.title("System Monitor")
root.geometry("300x150")

cpu_label = tk.Label(root, text="CPU Usage: N/A", font=("Arial", 12))
cpu_label.pack(pady=5)

memory_label = tk.Label(root, text="Memory Usage: N/A", font=("Arial", 12))
memory_label.pack(pady=5)

disk_label = tk.Label(root, text="Disk Usage: N/A", font=("Arial", 12))
disk_label.pack(pady=5)

update_gui()


root.mainloop()
