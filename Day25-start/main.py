import pandas

data = pandas.read_csv('weather_data.csv')
data_dict = data.to_dict()
# print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print(monday.temp[0] * 9/5 + 32)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv('students.csv')