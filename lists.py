names = [1, 2, "john", True]

names[1] = 'mary'

print(names)  # [1, 2, "john", True]

print(names[0])  # 1

print(names[-1])  # True

print(names[1])  # mary

print(names[0:3])  # 1 , 2, "john"


cars = ["honda", "bmw", "toyota", "volkswagen"]

cars.append("ford")

print(cars)

cars.insert(0, "porsche")

print(cars)

cars.remove("porsche")

print(cars)

cars.clear()

print(cars)

print("bmw" in cars)

print(len(cars))
