# server/stock_server.py
import sys
from xmlrpc.server import SimpleXMLRPCServer
sys.path.append('..')  # Add this line to include the project's root directory in the Python path

from common.stock_data import Stock

class StockServer:
    def __init__(self):
        self.stocks = [
            Stock("AAPL", 150.0, 10),
            Stock("GOOGL", 2500.0, 5),
            # Add more stocks as needed
        ]

    def get_stock_prices(self):
        return {stock.symbol: stock.price for stock in self.stocks}

    def buy_stock(self, symbol, quantity):
        # Implement buy logic here
        pass

    def sell_stock(self, symbol, quantity):
        # Implement sell logic here
        pass

if __name__ == "__main__":
    server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
    server.register_instance(StockServer())
    print("Server listening on port 8000...")
    server.serve_forever()
