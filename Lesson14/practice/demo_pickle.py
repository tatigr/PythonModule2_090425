import pickle
from typing import dataclass_transform

# write
# data = {"name": "Ivan", "age": 29, "salary": 35000}
#
# with open("save.bin", "wb") as file:
#     pickle.dump(data, file)


# read
with open("save.bin", "rb") as file:
    data = pickle.load(file)

print(data)