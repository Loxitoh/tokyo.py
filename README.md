# tokyo.py
Python library for interacting with Tokyo API (https://api.miduwu.ga/)

## Installation
`pip install git+https://github.com/Loxitoh/tokyo.py.git`

## Usage
```py
import tokyo
import asyncio
from tokyo.properties import Api

api = Api()
print(api.endpoints)

async def main():
  json = await tokyo.Json.get(endpoint = ..., builders = {
    ...
  })
  bytes = await tokyo.Buffer.get(endpoint = ..., builders = {
    ...
  })
  anime = await tokyo.Anime.get(endpoint = ..., builders = [
    ...
  ])
  print(json, bytes, anime)

  # Parameter "endpoint" is the request endpoint string.
  # Parameter "builders" is the request parameters/route. {} for parameters, [] for route.
  # await tokyo.Json.get(endpoint = '8ball', builders = {'text': 'Hi'})
  # await tokyo.Anime.get(endpoint = 'gifs', builders = ['angry'])

asyncio.run(main())
```
