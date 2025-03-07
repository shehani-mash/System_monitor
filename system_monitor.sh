#!/bin/bash

#function for display CPU  usage
cpu_Usage (){
	cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
	echo "CPU Usage: $cpu_usage%"
}

memory_Usage () {

	memory_usage=$(free -m | awk '/Mem:/ {printf "%.2f%%", $3/$2 * 100}')
	echo "Memory Usage: $memory_usage"
}

disk_Usage () {
	disk_usage=$(df -h / | awk '/\// {print $5}')
	echo "Disk Usage: $disk_usage"

}

monitor_system (){
	while true; do
		clear
		echo "Starting System Monitoring. Press Ctrl+c to exit..."
		echo "========System Monitor========"
		cpu_Usage
		memory_Usage
		disk_Usage
		echo "============================="
		sleep 5
	done
}

monitor_system
