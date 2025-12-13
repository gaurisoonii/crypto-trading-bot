from bot import BasicBot
from config import API_KEY, API_SECRET

def get_valid_input(prompt, cast_type=float, condition=lambda x: True):
    while True:
        try:
            value = cast_type(input(prompt))
            if condition(value):
                return value
            print("❌ Invalid value. Please try again.")
        except ValueError:
            print("❌ Invalid input type. Please try again.")

def get_order_side():
    while True:
        side = input("Order Side (BUY / SELL): ").upper()
        if side in ["BUY", "SELL"]:
            return side
        print("❌ Invalid side. Enter BUY or SELL.")

def get_symbol():
    while True:
        symbol = input("Trading Pair (e.g. BTCUSDT): ").upper()
        if symbol.endswith("USDT"):
            return symbol
        print("❌ Symbol must end with USDT.")

def confirm_order():
    confirm = input("Confirm order? (y/n): ").lower()
    return confirm == "y"

def main():
    print("\n" + "="*45)
    print("📊 BINANCE FUTURES TESTNET TRADING BOT")
    print("="*45)

    bot = BasicBot(API_KEY, API_SECRET)

    while True:
        print("\nChoose Order Type:")
        print("1️⃣  Market Order")
        print("2️⃣  Limit Order")
        print("3️⃣  Stop-Limit Order (Bonus)")
        print("4️⃣  Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "4":
            print("\n👋 Exiting bot. Happy Trading!")
            break

        if choice not in ["1", "2", "3"]:
            print("❌ Invalid choice.")
            continue

        symbol = get_symbol()
        side = get_order_side()
        quantity = get_valid_input("Quantity: ", float, lambda x: x > 0)

        print("\n📋 Order Summary")
        print("-" * 30)
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Quantity : {quantity}")

        try:
            if choice == "1":
                print("Type     : MARKET")
                if not confirm_order():
                    print("❌ Order cancelled.")
                    continue

                result = bot.place_market_order(symbol, side, quantity)

            elif choice == "2":
                price = get_valid_input("Limit Price: ", float, lambda x: x > 0)
                print(f"Type     : LIMIT @ {price}")

                if not confirm_order():
                    print("❌ Order cancelled.")
                    continue

                result = bot.place_limit_order(symbol, side, quantity, price)

            elif choice == "3":
                stop_price = get_valid_input("Stop Price: ", float, lambda x: x > 0)
                limit_price = get_valid_input("Limit Price: ", float, lambda x: x > 0)

                print("Type     : STOP-LIMIT")
                print(f"Stop     : {stop_price}")
                print(f"Limit    : {limit_price}")

                if not confirm_order():
                    print("❌ Order cancelled.")
                    continue

                result = bot.place_stop_limit_order(
                    symbol, side, quantity, stop_price, limit_price
                )

            print("\n✅ ORDER PLACED SUCCESSFULLY")
            print("-" * 30)
            print(f"Order ID : {result['orderId']}")
            print(f"Status   : {result['status']}")
            print(f"Type     : {result['type']}")
            print(f"Side     : {result['side']}")

        except Exception as e:
            print("\n❌ ORDER FAILED")
            print("Reason:", e)

if __name__ == "__main__":
    main()
