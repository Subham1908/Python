# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:32:44 2023

@author: YG168VL
"""
#1.1
def create_stock_portfolio():
    portfolio = {
        'AAPL': {'shares': 100, 'purchase_price': 150.25},
        'GOOG': {'shares': 50, 'purchase_price': 2500.75},
        'MSFT': {'shares': 75, 'purchase_price': 300.50},
        # Add more stocks as needed
    }
    return portfolio

# Call the function to create the stock portfolio dictionary
stock_portfolio = create_stock_portfolio()

# Example: Accessing information for a particular stock
print("AAPL shares:", stock_portfolio['AAPL']['shares'])
print("AAPL purchase price:", stock_portfolio['AAPL']['purchase_price'])

#1.2
def buy_stock(portfolio, stock_symbol, shares, purchase_price):
    if stock_symbol in portfolio:
        portfolio[stock_symbol]['shares'] += shares
        total_cost = portfolio[stock_symbol]['shares'] * portfolio[stock_symbol]['purchase_price']
        total_cost += shares * purchase_price
        total_shares = portfolio[stock_symbol]['shares']
        average_purchase_price = total_cost / total_shares
        portfolio[stock_symbol]['purchase_price'] = average_purchase_price
    else:
        portfolio[stock_symbol] = {'shares': shares, 'purchase_price': purchase_price}

# Example usage:
stock_portfolio = create_stock_portfolio()  # Assuming you have already created the stock portfolio
print("Portfolio before buying:", stock_portfolio)

buy_stock(stock_portfolio, 'AAPL', 50, 170.25)
buy_stock(stock_portfolio, 'GOOG', 25, 2450.50)
print("Portfolio after buying:", stock_portfolio)

#1.3
def sell_stock(portfolio, stock_symbol, shares_to_sell):
    if stock_symbol in portfolio:
        available_shares = portfolio[stock_symbol]['shares']
        if shares_to_sell <= available_shares:
            portfolio[stock_symbol]['shares'] -= shares_to_sell
            print(f"Sold {shares_to_sell} shares of {stock_symbol}.")
            if portfolio[stock_symbol]['shares'] == 0:
                del portfolio[stock_symbol]
        else:
            print("Not enough shares available to sell.")
    else:
        print("Stock symbol not found in the portfolio.")

# Example usage:
stock_portfolio = create_stock_portfolio()  # Assuming you have already created the stock portfolio
print("Portfolio before selling:", stock_portfolio)

sell_stock(stock_portfolio, 'AAPL', 25)
sell_stock(stock_portfolio, 'GOOG', 10)
print("Portfolio after selling:", stock_portfolio)

#1.4
import random

def calculate_portfolio_value(portfolio):
    total_value = 0
    for stock_symbol, stock_info in portfolio.items():
        purchase_price = stock_info['purchase_price']
        random_percentage = random.uniform(-20, 20)
        current_price = purchase_price + (random_percentage / 100) * purchase_price
        stock_value = stock_info['shares'] * current_price
        total_value += stock_value
        print(f"Stock: {stock_symbol}, Shares: {stock_info['shares']}, Current Price: {current_price:.2f}, Value: {stock_value:.2f}")
    return total_value

# Example usage:
stock_portfolio = create_stock_portfolio()  # Assuming you have already created the stock portfolio
print("Portfolio:", stock_portfolio)

portfolio_value = calculate_portfolio_value(stock_portfolio)
print("Total Portfolio Value:", portfolio_value)

#1.5
def portfolio_performance(initial_investment, current_value):
    percentage_change = ((current_value - initial_investment) / initial_investment) * 100
    return percentage_change

# Example usage:
stock_portfolio = create_stock_portfolio()  # Assuming you have already created the stock portfolio
print("Portfolio:", stock_portfolio)

initial_investment = 10000  # Set the initial investment value
current_value = calculate_portfolio_value(stock_portfolio)  # Assuming you have the current value of the portfolio
performance = portfolio_performance(initial_investment, current_value)
print("Portfolio Performance: {:.2f}%".format(performance))

#1.6
import random

def print_portfolio(portfolio):
    print("Current Portfolio:")
    for stock_symbol, stock_info in portfolio.items():
        print(f"Stock: {stock_symbol}, Shares: {stock_info['shares']}, Purchase Price: {stock_info['purchase_price']:.2f}")

def main():
    stock_portfolio = create_stock_portfolio()

    while True:
        print("\nMenu Options:")
        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. View Portfolio")
        print("4. Calculate Portfolio Value")
        print("5. Check Portfolio Performance")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            stock_symbol = input("Enter the stock symbol: ")
            shares = int(input("Enter the number of shares to buy: "))
            purchase_price = float(input("Enter the purchase price per share: "))
            buy_stock(stock_portfolio, stock_symbol, shares, purchase_price)

        elif choice == '2':
            stock_symbol = input("Enter the stock symbol: ")
            shares_to_sell = int(input("Enter the number of shares to sell: "))
            sell_stock(stock_portfolio, stock_symbol, shares_to_sell)

        elif choice == '3':
            print_portfolio(stock_portfolio)

        elif choice == '4':
            current_value = calculate_portfolio_value(stock_portfolio)
            print("Current Portfolio Value: {:.2f}".format(current_value))

        elif choice == '5':
            initial_investment = float(input("Enter the initial investment value: "))
            current_value = calculate_portfolio_value(stock_portfolio)
            performance = portfolio_performance(initial_investment, current_value)
            print("Portfolio Performance: {:.2f}%")





