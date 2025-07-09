from bot import BasicBot

def main():
    api_key = input("Enter your Binance Testnet API Key: ")
    api_secret = input("Enter your Binance Testnet API Secret: ")

    bot = BasicBot(api_key, api_secret)

    symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
    side = input("Buy or Sell: ").lower()
    order_type = input("Order type (MARKET / LIMIT): ").upper()
    quantity = float(input("Enter quantity: "))

    price = None
    if order_type == "LIMIT":
        price = float(input("Enter price: "))

    result = bot.place_order(symbol, side, order_type, quantity, price)
    if result:
        print("✅ Order placed successfully!")
        print("📄 Response:", result)
    else:
        print("❌ Failed to place order. Check logs for details.")

if __name__ == "__main__":
    main()
