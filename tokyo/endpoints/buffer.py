import aiohttp
from io import BytesIO
from ..properties import Api

class Buffer:
    '''
    Tokyo API buffer class

    Methods
    ----

    get: ClientResponse
        `Get the bytes response of the given endpoint`
    '''

    async def get(endpoint: str = None, builders: dict = None) -> aiohttp.ClientResponse:
        '''Get the bytes response of the given endpoint'''

        dictionary = Api().endpoints

        if endpoint is None:
            raise TypeError('Parameters cannot be empty.')
        elif builders is None:
            raise TypeError('Parameters cannot be empty.')
        elif not isinstance(builders, dict):
            raise TypeError('Innapropiate argument type (dict is required).')
        elif endpoint not in dictionary['BUFFER']:
            raise TypeError(f'Could not find endpoint "{endpoint}" in the buffer endpoints dictionary.')

        async with aiohttp.ClientSession() as session:
            async with session.get(url = f'{Api().base}/image/{endpoint}', params = builders) as response:
                return BytesIO(await response.read()).getvalue()
