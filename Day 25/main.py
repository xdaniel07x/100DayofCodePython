# with open("Day 25/weather_data.csv") as weather:
#     data = weather.readlines()
#     print(data)

# import csv

# with open("Day 25/weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
#     print(temperatures)

import pandas
