def forecast(*args):
    locations = {}
    for location, weather in args:
        if weather not in locations:
            locations[weather] = []
        locations[weather].append(location)
    sorted_locations = {}
    for weather in ["Sunny", "Cloudy", "Rainy"]:
        if weather in locations:
            sorted_locations[weather] = sorted(locations[weather])
    output = ""
    for weather in ["Sunny", "Cloudy", "Rainy"]:
        if weather in sorted_locations:
            for location in sorted_locations[weather]:
                output += f"{location} - {weather}\n"
    return output


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

