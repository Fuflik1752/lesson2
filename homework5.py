immutable_var = ("name", "age", 4, "height")
print(immutable_var)
mutable_list = ["name", "age", 4, "height"]
print(mutable_list)
mutable_list[0] = "weight"
print(mutable_list)

immutable_var[0] = "weight"
print(immutable_var)
