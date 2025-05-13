import json

# data = {"name": "Ivan", "age": 29, "salary": 35000}
#
# with open("save.json", "w") as file:
#     json.dump(data, file)

with open("save.json", "r") as file:
    result = json.load(file)

print(result)