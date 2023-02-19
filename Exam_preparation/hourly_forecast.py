def forecast(*args):
    result = []

    def add_location(type_of_weather):
        locations = list(filter(lambda x: x[1] == type_of_weather, args))
        [result.append(f"{l[0]} - {type_of_weather}") for l in sorted(locations)]

    add_location("Sunny")
    add_location("Cloudy")
    add_location("Rainy")

    return "\n".join(result)


# def forecast(*args):
#     result = []
#
#     def add_location(type_of_weather):
#         locations = []
#
#         for location, weather in args:
#             if weather == type_of_weather:
#                 locations.append(location)
#
#         for l in sorted(locations):
#             result.append(f"{l} - {type_of_weather}")
#
#     add_location("Sunny")
#     add_location("Cloudy")
#     add_location("Rainy")
#
#     return "\n".join(result)

# def forecast(*args):
#     locations = {}
#     for location, weather in args:
#         if weather not in locations:
#             locations[weather] = []
#         locations[weather].append(location)
#     sorted_locations = {}
#     for weather in ["Sunny", "Cloudy", "Rainy"]:
#         if weather in locations:
#             sorted_locations[weather] = sorted(locations[weather])
#     output = ""
#     for weather in ["Sunny", "Cloudy", "Rainy"]:
#         if weather in sorted_locations:
#             for location in sorted_locations[weather]:
#                 output += f"{location} - {weather}\n"
#     return output


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

