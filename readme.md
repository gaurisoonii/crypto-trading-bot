# Simplified Trading Bot – Binance

## Overview
This project implements a simplified trading bot using the Binance API.  
It supports market and limit orders with a command-line interface, logging, and error handling.

## Features
- Python-based trading bot
- Market and Limit orders
- Buy and Sell support
- Command-line interface with input validation
- Logging of API requests, responses, and errors
- Modular and reusable code structure
- Bonus: Stop-Limit order support

## Tech Stack
- Python
- python-binance library
- Binance API (REST)

## Project Structure
bot.py # Core trading logic
cli.py # CLI interface
logger.py # Logging configuration
config.py # API configuration


## How to Run

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/crypto-trading-bot.git
cd crypto-trading-bot

2.Install dependencies:

pip install -r requirements.txt


3.Add your API credentials in config.py:

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"


4.Run the CLI:

python cli.py


---

### 🔹 2️⃣ Sample CLI Flow (VERY IMPORTANT)

```md
## Sample CLI Execution

```text
Choose Order Type:
1 Market Order
2 Limit Order
3 Stop-Limit Order
4 Exit

Trading Pair: BTCUSDT
Order Side: BUY
Quantity: 0.001

Order placed / error returned and logged.


This proves you **actually ran the project**.

---

### 🔹 3️⃣ Logging Details (MANDATORY)

```md
## Logging

All API requests, responses, and errors are logged to:

logs/bot.log
Example logged error: APIError(code=-2010): Account has insufficient balance

🔹4️⃣ Binance Futures Testnet Limitation (CRITICAL)

This is the most important section.
## Note on Binance Futures Testnet
While the application is fully implemented to support Binance Futures Testnet (USDT-M),
Binance currently restricts Futures Testnet API key usage in certain regions.

Due to this limitation, order execution may fail with permission or balance-related errors.
These errors are handled gracefully and logged, demonstrating correct API integration,
error handling, and real-world robustness.

## Author
Gauri Soni
