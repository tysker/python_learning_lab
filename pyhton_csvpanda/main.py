# import csv
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data)
#     temperature = []
#
#     for row in data:
#         temp = int(row[1])
#         temperature.append(temp)
#
#     print(temperature)

import pandas

data = pandas.read_csv("./weather_data.csv")
# print(type(data))  # = DataFrame
# print(type(data["temp"]))  # = Series

# DataFrame type method
data_dict = data.to_dict()

# Series type method
avg = data["temp"].mean()
max = data["temp"].max()
data["temp"].to_list()

# Get data in coloumns
data["condition"]  # or
data.condition

# Get data in row
data[data.day == "Monday"]
print(data[data.temp == data.temp.max()])

# Convert celsius to fahrenheit
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9 / 5 + 32
print(monday_temp_f)

# Create dataframe from scratch
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
student_data = pandas.DataFrame(data_dict)
print(student_data)


# Data to csv
student_data.to_csv("student_list.csv")
