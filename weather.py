import requests
from datetime import datetime,timedelta
import csv
import os

datetime.now()
datetime.strftime
datetime.strptime
File_path = "weather_data.csv"

API_URL = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=precipitation_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
latitude = 53.331
longitude = -6.2489
timezone = 'Europe/London'

searched_date = input("Provide a date to check the weather (YYYY-mm-dd): ")

def get_next_day(date_str):
    date=datetime.strptime(date_str ,"%Y-%m-%d")
    next_day= date+ timedelta(days=1)
    return next_day.strftime ("%Y-%m-%d")

if not os.path.exists ("weather_date.csv"):
    with open (File_path,"w",newline="")as file:
        csv_writer= csv.writer(file)
        csv_writer.writerow(["Date","Precipitation Sum"])

if not searched_date:
    searched_date= get_next_day(datetime.now().strftime("%Y-%m-%d"))

with open(File_path,"r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row and row[0]== searched_date:
            precipitation_sum = float(row[1])
            break

    else:
        response= requests.get(API_URL.format(latitude=latitude, longitude=longitude, searched_date=searched_date))
        json_response=response.json()
        if 'daily' in json_response:
            daily_data=json_response['daily']
            precipitation_sum = daily_data['precipitation_sum'][0]
            if precipitation_sum > 0.0:
                with open(File_path,"a",newline="")as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow([searched_date,precipitation_sum])
        else:
            precipitation_sum = -1
    
if precipitation_sum > 0.0:
    print(f"It will rain. Precipitation Sum: {precipitation_sum}")
elif precipitation_sum == 0.0:
    print("It will not rain.")
else:
    print("I don't know.")
            
            







