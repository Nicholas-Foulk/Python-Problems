import threading
import time

exitFlag = 0

class MyNewThread(threading.Thread):
    def __init__(self,threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        print "Starting: " +self.name
        print_time(self.name, self.counter, 5)
        print "Exiting: " +self.name #sometimes these statements cause a space in the next printed line i think
                                     ##idk how to fix it
        
def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print"%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1
        
        
##here we instantiate the new threads

threadnum1 = MyNewThread(1001, "FirstThread", 2)
threadnum2 = MyNewThread(1002, "SecondThread", 5)


##start our new threads using the builtin method for 'threading' .start()

threadnum1.start()
threadnum2.start()
        
print "The program has started the threads."
        
