import pandas

data = pandas.read_csv(
    "Day 25/Squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = data["Primary Fur Color"]
black_fur = []
grey_fur = []
red_fur = []
for color in fur_color:
    if color == "Black":
        black_fur.append(color)
    elif color == "Gray":
        grey_fur.append(color)
    elif color == "Cinnamon":
        red_fur.append(color)

color_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [len(grey_fur), len(red_fur), len(black_fur)]
}

data = pandas.DataFrame(color_dict)
data.to_csv("Day 25/Squirrel/suirrel_count.csv")


# Alternative Solution:

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }

# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
