from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import mysql.connector
import uvicorn

#IDK WHY ITS SO FUCKED
#run with `uvicorn main:app`

global app 
app = FastAPI()


def main():


    print("test")

    soil_db = mysql.connector.connect(
        host = "localhost",
        user = "feb",
        password = "ubuntu",
        database = "soil"
    )

    my_cursor = soil_db.cursor()


    class sensor(BaseModel):
        sensor_id : int
        moisture : float
        time : str

    class dropdown(BaseModel):
        drop_val: int



    @app.post("/readings/")
    async def readings(item: sensor):

        sql = "INSERT INTO sensors (sensor_id, moisture, timestamp) VALUES (%s, %s, %s)"
        values = (item.sensor_id, item.moisture, item.time)
        my_cursor.execute(sql, values)
        soil_db.commit()
        print("\nData Entered into SQL Database\n")

        return item.sensor_id, item.moisture, item.time



    @app.post("/data")
    async def get_readings(item: dropdown):

        values = item.drop_val
        print("Sensor Values", values)

        moisture_sql = ("SELECT moisture FROM sensors WHERE sensor_id= (%s)") #currently just gives one but make this a variable 
        time_sql = ("SELECT timestamp FROM sensors WHERE sensor_id= (%s)")


        my_cursor.execute(moisture_sql, (values,))
        moisture_result = my_cursor.fetchall()

        my_cursor.execute(time_sql, (values,))
        time_result = my_cursor.fetchall()

        return(moisture_result, time_result)

main()