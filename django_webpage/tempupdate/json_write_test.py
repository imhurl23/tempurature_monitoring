# Luis Baez
# json_write_test.py
# used in one of the class demos
# script to continuously overwrite a JSON file which is used by views.py u

import time
import random

def overWriter():
    #runs for 5 minutes, changing the JSON values once every second
    for i in range(300):
        f = open("jsonEX.json", "w")
        temp1 = random.randint(32, 100)
        temp2 = random.randint(32, 100)
        ph = str(random.randint(0,13)) + "." + str(random.randint(0,99))
        jsonStr = f"{{\"temp1\":\"{temp1}\", \"temp2\":{temp2}, \"ph\":\"{ph}\"}}"
        print(jsonStr)
        f.write(jsonStr)
        f.close()
        time.sleep(1)

def main():
    overWriter()

if __name__ == "__main__":
    main()