class Cryptocurrency:
    def __init__(self,name,symbol,price):
        self.name = name
        self.symbol = symbol
        self.price = price
        
class Transaction:
    def __init__(self, crypto, quantity, transaction_type):
        self.crypto = crypto
        self.quantity = quantity
        self.transaction_type = transaction_type
        
class Wallet:
    def __init__(self):
        self.transactions = []
        
    def add_transaction(self, Transaction):
        self.transactions.append(Transaction)
        
    def display_wallet_history(self):
        for tran in self.transactions:
            print(f"{tran.transaction_type} {tran.crypto.symbol} - Quantity: {tran.quantity} - Current Value: {tran.quantity * tran.crypto.price}")
            
    def calculate_wallet_value(self):
        value = 0.0
        for tran in self.transactions:
            if tran.transaction_type == "buy":
                value += tran.quantity * tran.crypto.price
            elif tran.transaction_type == "sell":
                value -= tran.quantity * tran.crypto.price
                
        return value

def main():
    # Create instances of Cryptocurrency representing Bitcoin and Ethereum
    btc = Cryptocurrency("Bitcoin", "BTC", 50000.0)
    eth = Cryptocurrency("Ethereum", "ETH", 3000.0)
    # Create instances of Transaction representing buy and sell transactions
    transaction1 = Transaction(btc, 1.0, "buy")
    transaction2 = Transaction(eth, 2.0, "buy")
    transaction3 = Transaction(btc, 0.5, "sell")
    # Create an instance of Wallet
    my_wallet = Wallet()
    # Add transactions to the wallet
    my_wallet.add_transaction(transaction1)
    my_wallet.add_transaction(transaction2)
    my_wallet.add_transaction(transaction3)
    # Display history of the wallet
    my_wallet.display_wallet_history()
    # Calculate and print the total value of the wallet
    print(f"\nTotal Wallet Value: ${my_wallet.calculate_wallet_value():.2f}")
main()
    
    
            