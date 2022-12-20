import threading
import time
import array
import sys
import os

CurrentTemperature = array.array('i', [0, 0, 0, 0])
taskIsThere = 0
TemperaturePredicted1_3Ghz = 0
TemperaturePredicted2Ghz = 0
TriggerCount = 0

def computeTemp(TriggerCount):
	while(1):
		#print("Thread Number ", name , "Starting")
		with open(r"/sys/class/thermal/thermal_zone0/temp") as File:
			CurrentTemp_Core0 = File.readline()
			CurrentTemperature[0] = int(float(CurrentTemp_Core0) / 1000)

		with open(r"/sys/class/thermal/thermal_zone1/temp") as File:
			CurrentTemp_Core1 = File.readline()
			CurrentTemperature[1] = int(float(CurrentTemp_Core1) / 1000)

		with open(r"/sys/class/thermal/thermal_zone2/temp") as File:
			CurrentTemp_Core2 = File.readline()
			CurrentTemperature[2] = int(float(CurrentTemp_Core2) / 1000)

		with open(r"/sys/class/thermal/thermal_zone3/temp") as File:
			CurrentTemp_Core3 = File.readline()
			CurrentTemperature[3] = int(float(CurrentTemp_Core3) / 1000)


		if (TriggerCount == 10):
			print("Processing the Thread - Task Arrived")
			print("Current Temperature of Core-0 is :: ", CurrentTemperature[0], "deg Celsius")
			print("Current Temperature of Core-1 is :: ", CurrentTemperature[1], "deg Celsius")
			print("Current Temperature of Core-2 is :: ", CurrentTemperature[2], "deg Celsius")
			print("Current Temperature of Core-3 is :: ", CurrentTemperature[3], "deg Celsius")

			with open("./Temperature.txt", "r", encoding="utf-8") as g:
				TemperaturePredicted = list(map(int, g.readlines()))
					

			print("Temperature Predicted for 1.3Ghz (Core 0 & 1) ", TemperaturePredicted[0])
			print("Temperature Predicted for 2Ghz (Core 2 & 3) ", TemperaturePredicted[1])
			
			
			if ((TemperaturePredicted[0] - CurrentTemperature[0]) < 5):
				print("execute in core_0")
				os.system("taskset 1 python3 Task.py")
			elif ((TemperaturePredicted[0] - CurrentTemperature[1]) < 5):
				print("execute in core_1")
				os.system("taskset 2 python3 Task.py")
			elif ((TemperaturePredicted[1] - CurrentTemperature[2]) < 5):
				print("execute in core_2")
				os.system("taskset 4 python3 Task.py")
			elif ((TemperaturePredicted[1] - CurrentTemperature[3]) < 5):
				print("execute in core_3")
				os.system("taskset 8 python3 Task.py")
			else:
				print("Not Executed ", TemperaturePredicted1_3Ghz, TemperaturePredicted2Ghz)

			sys.exit("Program Executed Successfully !!!!!")

		TriggerCount += 1
		print(TriggerCount, " Waiting for Task to Arrive")
		time.sleep(1)

def main():
	x = threading.Thread(target=computeTemp, args=(TriggerCount,))
	x.start()
	
	x.join()
	
if __name__=="__main__":
	main()
