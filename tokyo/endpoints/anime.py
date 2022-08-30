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

    async def get(endpoint: str = None, parameters: dict = None) -> aiohttp.ClientResponse:
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
        elif parameters is None:
            raise TypeError('Parameters cannot be empty.')
        elif not endpoint == 'gifs' and not isinstance(parameters, dict):
            raise TypeError('Innapropiate argument type (dict is required).')
        elif endpoint == 'gifs' and not isinstance(parameters, list):
            raise TypeError('Innapropiate argument type (list is required).')
        elif endpoint not in dictionary['ANIME']:
            raise TypeError(f'Could not find endpoint "{endpoint}" in the anime endpoints dictionary.')
        elif endpoint == 'gifs' and parameters[0] not in allowed_gif_types:
            raise TypeError(f'Could not find gif type "{parameters[0]}" in the anime gif types list.')
        elif endpoint == 'gifs' and parameters[0] in allowed_gif_types:
            async with aiohttp.ClientSession() as session:
                async with session.get(url = f'{Api().base}/anime/{endpoint}/{parameters[0]}') as response:
                    return await response.json()
        elif endpoint == 'search':
            async with aiohttp.ClientSession() as session:
                async with session.get(url = f'{Api().base}/anime/{endpoint}', params = parameters) as response:
                    return await response.json()
