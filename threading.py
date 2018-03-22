
import thread
def func(a,b):
	while True:
		print a

def Main():
	a = 1
	b = 2
	thread.start_new_thread(func,(a,b))
	while True:
		print b
		
if __name__=="__main__":
	Main()


