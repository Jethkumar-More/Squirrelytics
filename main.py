import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirells_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirells_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirells_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirells_count)
print(gray_squirells_count)
print(gray_squirells_count)

data_dict = {
    "Fur Color" : ["Gray","Red","Black"],
    "Count" : [gray_squirells_count,red_squirells_count,black_squirells_count]
}

file = pandas.DataFrame(data_dict)
file.to_csv("DataSS")
