NON_REINFORCED_GAME_LIMIT = 1 #number of last non_reinforced_games. e.g if non_reinforced_game_limit is 2, the program will search for opponent who didn't reinforce defence his last 2 mines.

PRIVATE_KEYS = { #address : private key
    "0x82A323000D50CABaEd045A71FDE88e01a8b082d8":"58995c0f29e038d54d94868b8592edc1cbe88f076e24aa91b1a54b5d463317df"
}

ACCESS_TOKENS = { #address : access token of the address
    "0x82A323000D50CABaEd045A71FDE88e01a8b082d8":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7InVzZXJfYWRkcmVzcyI6IjB4ODJhMzIzMDAwZDUwY2FiYWVkMDQ1YTcxZmRlODhlMDFhOGIwODJkOCIsImVtYWlsX2FkZHJlc3MiOm51bGwsImZ1bGxfbmFtZSI6IkNyYWJhZGlhbiAxMmFiZGQ0YzQ1ZDgiLCJ1c2VybmFtZSI6bnVsbCwiZmlyc3RfbmFtZSI6bnVsbCwibGFzdF9uYW1lIjpudWxsfSwiaWF0IjoxNjYyNTM4MDg5LCJleHAiOjE2OTM2NDIwODksImlzcyI6IjZlYWI0ZTc5YTEwMzM0ZjU5MGY1NjQwMjY2ZjVkZWUxIn0.GncZBH9AnH_2h8MBWCZWpswl9fMa8ePOImQG8PhtEwk"
}
   
PRIVATE_KEYS_LIST = list(PRIVATE_KEYS.values())

GAS_PRICE_LIMIT = 20000 * pow(10,9)
GAS_LIMIT = 300000
MAX_PRIORITY_FEE_PER_GAS = 0

RPC_URL = "https://subnets.avax.network/swimmer/mainnet/rpc" #swimmer network
CHAIN_ID = 73772 #swimmer network
CONTRACT_ADDRESS = "0x9ab9e81Be39b73de3CCd9408862b1Fc6D2144d2B" #crabada_game_contract
