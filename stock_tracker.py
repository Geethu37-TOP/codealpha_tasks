import csv

def track_portfolio():
    # Hardcoded dictionary for stock prices as required
    stock_prices = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "MSFT": 320.0,
        "GOOGL": 140.0,
        "AMZN": 130.0
    }

    portfolio = {}
    total_investment = 0.0

    print("--- Welcome to the Stock Portfolio Tracker ---")
    print("Available stocks to track:", ", ".join(stock_prices.keys()))

    # Loop to capture user input
    while True:
        stock_name = input("\nEnter stock ticker (or type 'done' to finish): ").upper()

        if stock_name == 'DONE':
            break

        if stock_name not in stock_prices:
            print("Stock not found in our database. Please try an available ticker.")
            continue

        try:
            quantity = float(input(f"Enter quantity for {stock_name}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numerical value for quantity.")
            continue

        # Add or update the stock in the portfolio
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f"Successfully added {quantity} shares of {stock_name}.")

    # Calculate and display the final total
    print("\n--- Portfolio Summary ---")
    if not portfolio:
        print("No stocks were added to the portfolio.")
        return

    for stock, qty in portfolio.items():
        value = qty * stock_prices[stock]
        total_investment += value
        print(f"{stock}: {qty} shares @ ${stock_prices[stock]:.2f} = ${value:.2f}")

    print(f"\nTotal Investment Value: ${total_investment:.2f}")

    # Optional Scope: Save to CSV
    save_option = input("\nWould you like to save this summary to a CSV file? (yes/no): ").lower()
    if save_option == 'yes':
        with open("portfolio_summary.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], qty * stock_prices[stock]])
            writer.writerow(["", "", "Total Investment", total_investment])
        print("Portfolio saved successfully to 'portfolio_summary.csv'.")

if __name__ == "__main__":
    track_portfolio()
