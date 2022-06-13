from mega import Mega
from datetime import datetime
import os
import time

m = Mega()
usr = m.login("uploadme@yopmail.com","Bhaibhai45")

while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        fname = "Time " + str(current_time) + ".txt"

        with open(fname,"w") as f:
                f.write(current_time)

        usr.upload(fname)
        print(":: Uploaded file !")
        os.remove(fname)
