import threading
my_file=("temp.txt")
def print_python():
	exec(open("python.py").read())
def print_temp():
	my_file=open("temp.txt","r")
print(my_file.read())
if _name_=="_main_":
	t1=threading.Thread(target=print_python,args=(10,))
	t2=threading.Thread(target=print_temp,args=(10,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Done!")
