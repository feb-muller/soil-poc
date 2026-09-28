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


    @app.post("/readings/")
    async def readings(item: sensor):

        sql = "INSERT INTO sensors (sensor_id, moisture, timestamp) VALUES (%s, %s, %s)"
        values = (item.sensor_id, item.moisture, item.time)
        my_cursor.execute(sql, values)
        soil_db.commit()
        print("\nData Entered into SQL Database\n")

        return item.sensor_id, item.moisture, item.time



    @app.get("/data")
    async def get_readings():
        sql = ("SELECT * FROM sensors WHERE sensor_id= 1") #currently just gives one but make this a variable 

        my_cursor.execute(sql)
        result = my_cursor.fetchall()

        return(result)

main()