# SHU Smart Irrigation Management System #
The project proposed would be a monitoring system for plant soil moisture, stopping plants dieback due to heat stress in the UK’s greenest city.

`Sensors -> REST API -> Database -> Data Processing -> Web Dashboard-> Alerts System`

**Sensors**: Using python scripts and a JSON format hundreds of sensors can be simulated at once with a large variety of test data available. Once simulated, physical devices can be implemented through hardware like Raspberry Pi’s or ESP32 microcontrollers.

**REST API Container**: A REST API deployed using containerization for environment management and consistency, API takes ‘sensor’ readings evaluates and verifies them then passes them to a Database for long term history tracking.

**Database Container**: Tracking changes in soil moisture levels over a large period allows quick access to anomalous data and analytics of patterns.

**Data Processing Container**: This end of the project is concerned with manipulating the database into presentable outputs such as averages and graphs using the Pandas and Matplotlib libraries. 

**Web Frontend**: A web dashboard allowing concerned parties to view and manage the data by adjusting watering patterns accordingly.

**Alert System**: Connected to the Web Frontend is an alert system where outlying data can be flagged and reported for further consideration.
