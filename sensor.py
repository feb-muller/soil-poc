import requests
from datetime import datetime
import random

def main():
    for i in range(10):

        time = datetime.now().strftime('%H:%M:%S')

        print(time)

        moisture = random.randint(0,100)
        timestamp = str(time)

        data = {
            "sensor_id" : i,
            "moisture" : moisture,
            "time" : timestamp
        }

        response = requests.post(
            "http://172.16.15.73:8000/readings/",
            json = data
        )
        print(response.json())

if __name__ == '__main__':
    main()