from binance import Client
from binance.exceptions import BinanceAPIException
from logger import logger

class BasicBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        logger.info("Connected to Binance SPOT API")

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logger.info(order)
            return order
        except BinanceAPIException as e:
            logger.error(e)
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )
            logger.info(order)
            return order
        except BinanceAPIException as e:
            logger.error(e)
            raise
