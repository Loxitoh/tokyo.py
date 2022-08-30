class Api():
    '''
    Tokyo API properties class

    Attributes
    ----

    endpoints: dict
        `Returns all API endpoints`
    base: str
        `Returns API base URL`
    discord_server: str
        `Returns API discord server's URL`
    json_count: int
        `Returns API json endpoints count`
    buffer_count: int
        `Returns API buffer endpoints count`
    total_count: int
        `Returns API total endpoints count`
    '''

    def __init__(self) -> None:
        pass

    @property
    def endpoints(self) -> dict:
        '''Returns all API endpoints.'''
        return {
            'JSON': [
                '8ball',
                'ascii',
                'binary',
                'coinflip',
                'define',
                'discorduser',
                'gis',
                'github',
                'hastebin',
                'minecraft',
                'npm',
                'owoify',
                'repository',
                'reverse',
                'time',
                'topgg',
                'translate',
                'weather'
            ],
            'ANIME': [
                'gifs',
                'search',
            ],
            'BUFFER': [
                'bart',
                'beautiful',
                'blur',
                'boost',
                'circle',
                'clash',
                'color',
                'communism',
                'deepfry',
                'delete',
                'discordjs',
                'eject',
                'gay',
                'gray',
                'hollywood',
                'invert',
                'mad',
                'magik',
                'mexico',
                'overlay',
                'pixel',
                'rankcard',
                'rip',
                'santa',
                'ship',
                'shit',
                'simp',
                'sonic',
                'spotify',
                'supreme',
                'sus',
                'tweet',
                'walletcard',
                'wanted',
                'welcomecard',
                'whoreallyare'
            ]
        }

    @property
    def base(self) -> str:
        '''Returns API base URL'''
        return 'https://api.miduwu.ga'

    @property
    def discord_server(self) -> str:
        '''Returns API discord server's URL'''
        return 'https://discord.com/invite/3pT2WHG9EG'

    @property
    def json_count(self) -> int:
        '''Returns API JSON endpoints count'''
        return 18

    @property
    def buffer_count(self) -> int:
        '''Returns API buffer endpoints count'''
        return 36

    @property
    def total_count(self) -> int:
        '''Returns API total endpoints count'''
        return Api().json_count + Api().buffer_count