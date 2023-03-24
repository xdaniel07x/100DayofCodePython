# import another_module
# from turtle import Turtle, Screen
from prettytable import PrettyTable

# # print(another_module.another_variable)

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.fillcolor("green2")
# # timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)

# # index = 25

# # for _ in range(5):
# #     timmy.circle(index)
# #     index += 25

# my_screen.exitonclick()

tables = PrettyTable()

tables.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
tables.add_row(["Adelaide", 1295, 1158259, 600.5])
tables.add_row(["Brisbane", 5905, 1857594, 1146.4])
tables.add_row(["Darwin", 112, 120900, 1714.7])
tables.add_row(["Hobart", 1357, 205556, 619.5])
tables.add_row(["Sydney", 2058, 4336374, 1214.8])
tables.add_row(["Melbourne", 1566, 3806092, 646.9])
tables.add_row(["Perth", 5386, 1554769, 869.4])
tables.align = "l"

print(tables)
