# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130
}

total_investment = 0
portfolio = {}

print("Available stocks:", list(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock] = quantity
    else:
        print("Stock not available.")

# Calculate investment
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value

print("\nPortfolio Summary:")
for stock, qty in portfolio.items():
    print(stock, "x", qty, "=", stock_prices[stock] * qty)

print("Total Investment Value:", total_investment)

# Optional: save to file
with open("portfolio.txt", "w") as file:
    file.write("Portfolio Summary\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock} x {qty} = {stock_prices[stock]*qty}\n")
    file.write(f"Total Investment: {total_investment}")