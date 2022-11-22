import blockcypher
token = "a6a9729a09c24da2b02491d9d521f5f3"
last_height = blockcypher.get_latest_block_height(coin_symbol='bcy',api_key=token)
print("The latest BCY block height is:", last_height)