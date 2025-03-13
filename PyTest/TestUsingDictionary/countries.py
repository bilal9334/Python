capitals = {
    "Germany": "Berlin",
    "France": "Paris",
    "Italy": "Rome",
    "Spain": "Madrid",
}

def get_capital(country: str, data: dict) -> str:
    if country in data:
        return data[country] # This would return the value of the passes key
    else:
        return "Country not found"
    


city = get_capital("Germany", capitals)
print(city)