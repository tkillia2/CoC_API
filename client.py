from pip._vendor import requests


class cocClient:
    def __init__(self, host, token):
        self.host = host
        self.token = token
    
    def getClanCurrentWar(self, clanTag):
        response = requests.get(f'{host}/clans/{clanTag}/currentwar', host, clanTag)
        return response.json