import requests
import json
import pprint

#URL pointing to API for Chuck Norris Joke
url = "https://api.chucknorris.io/jokes/random"

#API Stuff
payload = {}
headers = {
  'Cookie': '__cfduid=dfdec38580fe5f1e2d334cf00bb15788a1600985684'
}

#Send GET Request to URL, then parse JSON into dictionary
response = requests.request("GET", url, headers=headers, data = payload)
json_response = response.json()
chuck = json_response['value']

#Welcome user to CHuck Norris machine!
print("Welcome to the Chuck Norris machine!")
print('Would you Like to here a Chuck Norris Joke?')

while True:
    response = input('Yes or No:')
    response = response.strip()
    response = response.lower()
    if response == "yes":
        print('.......')
        print(chuck)
        break
    elif response == "no":
        print('.......')
        print("No one denies Chuck Norris. Here you go anyways:")
        print(chuck)
        break
    else:
        print('.......')
        print("It doesn't matter what you answer. Here you go:")
        print(chuck)
        break