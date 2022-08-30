import aiohttp
from ..properties import Api

class Json:
    '''
    Tokyo API JSON class

    Methods
    ----

    get: ClientResponse
        `Get the JSON response of the given endpoint`
    '''

    async def get(endpoint: str = None, builders: dict = None) -> aiohttp.ClientResponse:
        '''Get the JSON response of the given endpoint'''

        dictionary = Api().endpoints

        if endpoint is None:
            raise TypeError('Parameters cannot be empty.')
        elif builders is None:
            raise TypeError('Parameters cannot be empty.')
        elif not isinstance(builders, dict):
            raise TypeError('Innapropiate argument type (dict is required).')
        elif endpoint not in dictionary['JSON']:
            raise TypeError(f'Could not find endpoint "{endpoint}" in the JSON endpoints dictionary.')

        async with aiohttp.ClientSession() as session:
            async with session.get(url = f'{Api().base}/json/{endpoint}', params = builders) as response:
                return await response.json()
