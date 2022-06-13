from mega import Mega
from datetime import datetime
import os
import time
import psutil

m = Mega()
usr = m.login("uploadme@yopmail.com","Bhaibhai45")

while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        fname = "Time " + str(current_time) + ".txt"

        with open(fname,"w") as f:
                f.write(current_time)
                hdd = psutil.disk_usage('/')
                f.write("Total: %d GiB" % hdd.total / (2**30))
                f.write("Used: %d GiB" % hdd.used / (2**30))
                f.write("Free: %d GiB" % hdd.free / (2**30))


        usr.upload(fname)
        print(":: Uploaded file !")
        os.remove(fname)
