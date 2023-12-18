# from turtle import *

# test =Turtle()
# print(test.pen)
# #in here test is an object, turtle is a class
# #pen is an an attributes of the object
# test.shape("turtle")
# test.color("blue")
# test.forward(100)


# shiny = Screen()
# shiny.exitonclick()
from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes
# x = PrettyTable()
# x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# x.add_row(["Adelaide", 1295, 1158259, 600.5])
# x.add_row(["Brisbane", 5905, 1857594, 1146.4])
# x.add_row(["Darwin", 112, 120900, 1714.7])
# x.add_row(["Hobart", 1357, 205556, 619.5])
# x.add_row(["Sydney", 2058, 4336374, 1214.8])
# x.add_row(["Melbourne", 1566, 3806092, 646.9])
# x.add_row(["Perth", 5386, 1554769, 869.4])
# print(x)
table = ColorTable(theme=Themes.OCEAN)
table.field_names = ["pokeman_name", "Type"]
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmander","Fire"])
print(table)