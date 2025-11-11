import requests
import pprint as pp

latitude = 35.7014
longitude = 59.8466

# Making an HTTP Request from the API
# response = requests.get('https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400').text  # type is str

# print(response)


# Creating a Python Dictionary
response_info = requests.get(
    f'https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}').json()  # type is dict

# print(response_info)

# Parsing the Dictionary
pp.pprint(response_info["results"])
# print(response_info["status"])
