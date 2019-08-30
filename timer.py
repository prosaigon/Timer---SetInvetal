# code by MrDzo 2019-08-30
# Timer / SetInvetal

import threading
import time

class Timer:
    def __init__(self,secords = None,function = None,args=(), kwargs={}):
        self.function = function
        self.secords = secords
        self.args = args
        self.kwargs = kwargs
        self.stop = False

    def Start(self):
        print("[Timer] : starting")
        self.thread = threading.Thread(target=self.Worker,args=())
        # self.thread.daemon = True
        self.thread.start()

    def Worker(self):
        while True:
            try:
                if self.function:
                    self.function(*self.args, **self.kwargs)
                    time.sleep(self.secords)
                    if self.stop is True:
                        break
            except Exception as ex :
                raise ex

    def Stop(self):
        self.stop = True
        print("[Timer] : stop")