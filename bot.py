import logging
from binance.client import Client
from binance.enums import *
from logger import setup_logger

logger = setup_logger()

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        logger.info("Initialized Binance client (Testnet: %s)", testnet)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                "symbol": symbol,
                "side": SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == ORDER_TYPE_LIMIT:
                params["price"] = price
                params["timeInForce"] = TIME_IN_FORCE_GTC

            order = self.client.futures_create_order(**params)
            logger.info("Order placed: %s", order)
            return order

        except Exception as e:
            logger.error("Order failed: %s", str(e))
            return None
