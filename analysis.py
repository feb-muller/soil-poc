import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


soil_db = mysql.connector.connect(
    host = "localhost",
    user = "feb",
    password = "ubuntu",
    database = "soil"
)


my_cursor = soil_db.cursor()

sql = ("SELECT * FROM sensors WHERE sensor_id= 1")
sensor_id= 1 #MAKES A GRAPH FOR WHATEVER THIS ID NUMBER IS!
moisture = []
timestamp = []

my_cursor.execute(sql)
result = my_cursor.fetchall()

for x in result:
    moisture.append(x[2])
    timestamp.append(x[3])

print(moisture)
print(timestamp)

plt.plot(timestamp,moisture)
plt.xlabel('Time')
plt.ylabel('Moisture (%)')
plt.title('Sensor 1 Moisture Levels')
plt.savefig("test_fig.png", dpi=200)

soil_db.commit()


''' CALCULATING AVERAGE FROM result VARIABLLE
    total_moisture = 0
    counter = 0
    for x in result:
        moisture = x[0]
        total_moisture += moisture
        counter += 1

    average_moisture = total_moisture/counter
    print(f"\nThe average moisture for sensor {i} is {average_moisture}.")
'''
