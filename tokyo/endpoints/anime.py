import aiohttp
from ..properties import Api

class Anime:
    '''
    Tokyo API anime class

    Methods
    ----

    get: ClientResponse
        `Get the JSON response of the given endpoint`
    '''

    async def get(endpoint: str = None, builders: dict = None) -> aiohttp.ClientResponse:
        '''Get the JSON response of the given endpoint'''

        dictionary = Api().endpoints
        allowed_gif_types = [
            'angry',
            'baka',
            'bite',
            'blush',
            'cry',
            'dance',
            'deredere',
            'happy',
            'hug',
            'kiss',
            'path',
            'punch',
            'slap',
            'sleep',
            'smug'
        ]

        if endpoint is None:
            raise TypeError('Parameters cannot be empty.')
        elif builders is None:
            raise TypeError('Parameters cannot be empty.')
        elif not endpoint == 'gifs' and not isinstance(builders, dict):
            raise TypeError('Innapropiate argument type (dict is required).')
        elif endpoint == 'gifs' and not isinstance(builders, list):
            raise TypeError('Innapropiate argument type (list is required).')
        elif endpoint not in dictionary['ANIME']:
            raise TypeError(f'Could not find endpoint "{endpoint}" in the anime endpoints dictionary.')
        elif endpoint == 'gifs' and builders[0] not in allowed_gif_types:
            raise TypeError(f'Could not find gif type "{builders[0]}" in the anime gif types list.')
        elif endpoint == 'gifs' and builders[0] in allowed_gif_types:
            async with aiohttp.ClientSession() as session:
                async with session.get(url = f'{Api().base}/anime/{endpoint}/{builders[0]}') as response:
                    return await response.json()
        elif endpoint == 'search':
            async with aiohttp.ClientSession() as session:
                async with session.get(url = f'{Api().base}/anime/{endpoint}', params = builders) as response:
                    return await response.json()
