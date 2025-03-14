climate_data = {
    "1990": {"anomaly": 0.42, "uncertainty": 0.05},
    "1991": {"anomaly": 0.48, "uncertainty": 0.06},
    "1992": {"anomaly": 0.14, "uncertainty": 0.07},
    "1993": {"anomaly": 0.27, "uncertainty": 0.04},
    "1994": {"anomaly": 0.32, "uncertainty": 0.05}
}

# Task: Loop through the dictionary and print each year with its anomaly value
# for year, data in climate_data.items():
#     value = data['anomaly']
#     print(f"{year} ... {value}")

# Task: Find the year with the highest anomaly and print it
# max_anomaly = float('-inf')
# max_year = None
#
# for year, data in climate_data.items():
#     value = data['anomaly']
#     if value > max_anomaly:
#         max_anomaly = value
#         max_year = year
#
# print(f"The highest anomaly was in {max_year} with a value of {max_anomaly}")

# Task: Print only years when the anomaly was greater than 0.3
max_anomaly = float('-inf')

# for year, data in climate_data.items():
#     value = data['anomaly']
#     if value > 0.3:
#         max_anomaly = value
#         print(f"{year} ... {max_anomaly}")

# Task: Convert the dictionary into a list of (year, anomaly) tuples
result = [(year, anomaly['anomaly']) for year, anomaly in climate_data.items()] # Comprehension to convert to dict to tuples
print(result)
