my_dict = {"city": "Москва", "temperature": "20"}
print(my_dict["city"])
my_dict["temperature"] = str(int(my_dict["temperature"]) - 5)

for k, v in my_dict.items():
    print(f"{k} : {v}")

if "country" in my_dict:
    print(True)
else:
    print(False)

print(my_dict.get("country", "Россия"))
my_dict["date"] = "27.05.2017"
print(len(my_dict))
