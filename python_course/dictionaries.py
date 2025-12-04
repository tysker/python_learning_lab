my_first_dic = {
    1: "this os the first one",
    2: "this is the second one",
    3: "this is the third one",
}

print(my_first_dic[1])
my_first_dic[4] = "this is the fourth one"

print(my_first_dic)

travel_log = {
    "Germany": ["Berlin", "Stuttgart", "Köln"]
}

town = travel_log["Germany"][0]
print(town)

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][0]) # C

travel_logs = {
    "France": {
            "cities_visited": ["Paris", "Lille", "Dijon"],
            "total_visits": 12
        },
    "Germany": {
        "cities_visited": ["Berlin", "Stuttgart", "Köln"],
        "total_visits": 5
        }
}

print(travel_logs["Germany"]["cities_visited"][2])


