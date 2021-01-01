import logic as c
from logic import create, delete, read
from threading import Thread
# code is the file name of the file as a library

c.create("Prasanna", 50, 120)
c.read("Prasanna")
c.delete("Prasanna")

tre1 = Thread(target=(create or read or delete),
              args=(key_name, value, timeout))
tre1.start()
tre1.sleep()
tre2 = Thread(target=(create or read or delete),
              args=(key_name, value, timeout))
tre2.start()
tre2.sleep()
