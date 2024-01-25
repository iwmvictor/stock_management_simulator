# client/stock_client.py
import xmlrpc.client

class StockClient:
    def __init__(self):
        self.server = xmlrpc.client.ServerProxy("http://localhost:8000")

    def get_stock_prices(self):
        return self.server.get_stock_prices()

    def buy_stock(self, symbol, quantity):
        return self.server.buy_stock(symbol, quantity)

    def sell_stock(self, symbol, quantity):
        return self.server.sell_stock(symbol, quantity)

if __name__ == "__main__":
    client = StockClient()
    
    # Example usage:
    stock_prices = client.get_stock_prices()
    print("Stock Prices:", stock_prices)

    # Add more interactions as needed
