import requests
import json
import dotenv
import os

dotenv.load_dotenv()

url = "https://api.trello.com/1/cards"

headers = {
  "Accept": "application/json"
}

query = {
  'idList': '668592d4fcea1b06ea415887',
  'key': os.getenv("API_KEY"),
  'token': os.getenv("API_TOKEN"),

  'name': '@discorduser',
  'description': "the description provided by the user",
  'idLabels': []
}

response = requests.request(
   "POST",
   url,
   headers=headers,
   params=query
)

print(response.text)