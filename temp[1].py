import threading
import decimal
arr=[]
core_1=open("/sys/class/thermal/thermal_zone0/temp")
print(core_1.read())
core_2=open("/sys/class/thermal/thermal_zone1/temp")
print(core_2.read())
core_3=open("/sys/class/thermal/thermal_zone2/temp")
print(core_3.read())
core_4=open("/sys/class/thermal/thermal_zone3/temp")
print(core_4.read())
#arr[0]=core_1.read()/1000;
core_1temp=core_1.read()
core_1temp = core_1temp
#print(int(core_1.read()))
print(type(core_1.read()))
