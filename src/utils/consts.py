METHODS = {
    "attack":"0x77728f25",
    "settle":"0x312d7bbc",
    "startGame":"0xe5ed1d59",
    "reinforceDefense":"0x08873bfb",
    "closeGame":"0x2d6ef310",
    "reinforceAttack":"0x3dc8d5ce",
    }

ADVANTAGES = {
    "LUX":["FAERIE","ORE"],
    "FAERIE":["ORE","ABYSS"],
    "ORE":["ABYSS","TRENCH"],
    "ABYSS":["TRENCH","MACHINE"],
    "TRENCH":["MACHINE","LUX"],
    "MACHINE":["LUX","FAERIE"],
    "NO_FACTION":[],
}

HEADERS = {
    'authority': 'idle-game-api.crabada.com',
    'accept': 'application/json, text/plain, /',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'origin': 'https://idle.crabada.com',
    'pragma': 'no-cache',
    'referer': 'https://idle.crabada.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36',
}

GAS_PRICE_LIMIT = 20000 * pow(10,9)
GAS_LIMIT = 300000
RPC_URL = "https://subnets.avax.network/swimmer/mainnet/rpc"
CHAIN_ID = 73772
CONTRACT_ADDRESS = "0x9ab9e81Be39b73de3CCd9408862b1Fc6D2144d2B" #crabada_game_contract
