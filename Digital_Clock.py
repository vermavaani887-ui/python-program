from datetime import datetime
import time

while True:
    current_time = datetime.now().strftime("%H:%M:%S")

    print("\rCurrent Time:", current_time, end="")

    time.sleep(1)
