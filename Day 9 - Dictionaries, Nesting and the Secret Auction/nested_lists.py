capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# print Lille

# print(travel_log["France"][1])

# Nested List

nested_list = ["A", "B", ["C", "D"]]

# Print D in the nested list

print(nested_list[2][1])


travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart", ],
        "total_visits": 5
    },
}

# Print Stuttgart

print(travel_log["Germany"]["cities_visited"][2])