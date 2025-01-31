import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_color = len(data[data["Primary Fur Color"] == "Gray"])
red_color = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color = len(data[data["Primary Fur Color"] == "Black"])
print(grey_color)
print(red_color)
print(black_color)

squirrel_count = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "count": [grey_color,red_color,black_color]
}
squirrel_data = pandas.DataFrame(squirrel_count)
squirrel_data.to_csv("squirrel count based on color")

