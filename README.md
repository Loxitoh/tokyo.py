# tokyo.py
Python library for interacting with Tokyo API (https://api.miduwu.ga/)

## Installation
`pip install git+https://github.com/Loxitoh/tokyo.py.git`

## Example
```py
import tokyo
import asyncio

async def main():
  json = await tokyo.Json.get(endpoint = '8ball', builders = {
    'text': 'Am I gay?'
  })
  bytes = await tokyo.Buffer.get(endpoint = 'bart', builders = {
    'text': 'Hi'
  })
  anime = await tokyo.Anime.get(endpoint = 'gifs', builders = [
    'angry'
  ])
  print(json, bytes, anime)

asyncio.run(main())
```
