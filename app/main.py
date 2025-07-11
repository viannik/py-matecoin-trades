import decimal
import json


def calculate_profit(trades: str) -> None:
    total_earned = 0
    total_balance = 0
    with open(trades, "r") as trades_file:
        trades_data = json.load(trades_file)
        for trade in trades_data:
            bought = decimal.Decimal(trade.get("bought") or "0")
            sold = decimal.Decimal(trade.get("sold") or "0")
            price = decimal.Decimal(trade.get("matecoin_price") or "0")

            total_earned += (sold - bought) * price
            total_balance += bought - sold

    with open("profit.json", "w") as profit_file:
        profit_data = {
            "earned_money": str(total_earned),
            "matecoin_account": str(total_balance),
        }
        json.dump(profit_data, profit_file, indent=4)


if __name__ == "__main__":
    calculate_profit("trades.json")
    print("Profit calculation completed. Check profit.json for results.")
