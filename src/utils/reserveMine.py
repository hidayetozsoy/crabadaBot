import requests
from config import ACCESS_TOKENS

def getHeaders(accessToken, gameId):
    headers = {
    'authority': 'idle-game-api.crabada.com',
    'method': 'PUT',
    'path': f'/public/idle/attack/{gameId}',
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,tr-TR;q=0.8,tr;q=0.7',
    'authorization': f'Bearer {accessToken}',
    'content-length': '15',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://idle.crabada.com',
    'referer': 'https://idle.crabada.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'macOS',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    return headers

def reserveMine(accessToken, gameId, teamId):
    attackUrl = f"https://idle-game-api.crabada.com/public/idle/attack/{gameId}"
    data = {"team_id":teamId}
    headers = getHeaders(accessToken, gameId)
    response = requests.put(attackUrl, json=data, headers=headers)
    
if __name__ == "__main__":
    reserveMine(ACCESS_TOKENS["0xb945f4Cc708A74b8f7FC70d689e445cdEb9bC9f4"], 2577893, 545)
    