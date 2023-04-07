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

data = pandas.read_csv("Day 25/weather_data.csv")
print(type(data))
print(data["temp"])

data_dict = data.to_dict()
temp_list = data["temp"].to_list()

print(temp_list)
print(len(temp_list))
print(data["temp"].mean())
print(data["temp"].max())

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday = data[data.day == "Monday"]
temp = monday.temp
fahrenheit = float((temp * 9 / 5) + 32)
print(fahrenheit)

# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("Day 25/new_data.csv")
