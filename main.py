from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import mysql.connector

def main():
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

    app = FastAPI()

    @app.post("/readings/")
    async def readings(item: sensor):
        print(item)

        sql = "INSERT INTO sensors (sensor_id, moisture, timestamp) VALUES (%s, %s, %s)"
        values = (item.sensor_id, item.moisture, item.time)
        my_cursor.execute(sql, values)
        soil_db.commit()
        print("\nData Entered into SQL Database\n")

        return item.sensor_id, item.moisture, item.time

    
if __name__ == '__main__':
    main()