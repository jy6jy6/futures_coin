import ccxt
import json

def get_mexc_future_coins():
    try:
        exchange = ccxt.mexc({'options': {'defaultType': 'future'}})
        markets = exchange.load_markets()
        
        future_coins = sorted(set([
            market.split('/')[0] for market in markets 
            if markets[market].get('future') or markets[market].get('swap')
        ]))
        
        print(f"Successfully fetched {len(future_coins)} future coins from MEXC using CCXT")
        return future_coins
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return []

if __name__ == "__main__":
    future_coins = get_mexc_future_coins()
    if future_coins:
        with open('future_coins.json', 'w') as f:
            json.dump(future_coins, f, indent=2)
        print("Successfully created future_coins.json")
