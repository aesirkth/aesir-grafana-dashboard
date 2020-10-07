from influxdb import InfluxDBClient
from datetime import datetime

def initDB():
    now = datetime.now()
    time = now.strftime("%Y-%m-%d-%H:%M:%S")
    dbClient = InfluxDBClient(host='localhost', port='8086')

    #create a new database
    dbClient.drop_database("Mjollnir")
    dbClient.create_database("Mjollnir")
    dbClient.switch_database("Mjollnir")

    #create a new retention policy
    return dbClient

def handleData(data, dbClient, time):
    points = []
    for v in data:
        point = {
            "measurement": v.source,
            "tags": {
                #none
            },
            #"time": time,
            "fields": {
                v.measurement: v.value,
                #"flight_time": time
            }
        }
        points.append(point)
    dbClient.write_points(points)
    return 0
    