# tokyo.py
Python library for interacting with Tokyo API (https://api.miduwu.ga/)

## Installation
`pip install git+https://github.com/Loxitoh/tokyo.py.git`

## Usage
```py
import tokyo
import asyncio

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

asyncio.run(main())
```
