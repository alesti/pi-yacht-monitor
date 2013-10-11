import time
import storagehandler

timestamp = int(time.time())
storagehandler.save("boat.time",timestamp)

