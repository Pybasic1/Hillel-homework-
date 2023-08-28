'''lesson8'''

import requests
import argparse
import datetime
from tabulate import tabulate

API_URL = "https://api.exchangerate.host/convert"
SYMBOLS_FILE = "symbols.json"

def get_symbols():
    with open(SYMBOLS_FILE) as f:
        symbols_data = json.load(f)
        return symbols_data.get("symbols", [])

def get_exchange_rate(date, from_currency, to_currency):
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": 1,
        "date": date
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("result", None)
    else:
        return None

def convert_currency(from_currency, to_currency, amount, start_date, save_to_file):
    symbols = get_symbols()
    if from_currency not in symbols or to_currency not in symbols:
        print("Невірний символ валюти.")
        return

    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    if start_date > current_date:
        start_date = current_date

    exchange_rates = [["date", "from", "to", "amount", "rate", "result"]]
    date_iter = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    while date_iter <= datetime.datetime.now():
        date_str = date_iter.strftime('%Y-%m-%d')
        rate = get_exchange_rate(date_str, from_currency, to_currency)
        if rate is None:
            print("Помилка отримання курсу валют.")
            return
        result = amount * rate
        exchange_rates.append([date_str, from_currency, to_currency, amount, rate, result])
        date_iter += datetime.timedelta(days=1)

    if save_to_file:
        filename = f"{start_date}-{from_currency}-{to_currency}-{len(exchange_rates)-1}-days-weather-forecast.txt"
        with open(filename, 'w') as f:
            f.write(tabulate(exchange_rates, headers="firstrow"))
        print(f"Прогноз погоди збережено у файлі '{filename}'.")
    else:
        print(tabulate(exchange_rates, headers="firstrow"))

def main():
    parser = argparse.ArgumentParser(description="Онлайн конвертер валют")
    parser.add_argument("currency_from", type=str, default="USD", help="Валюта для конвертації з")
    parser.add_argument("currency_to", type=str, default="UAH", help="Валюта для конвертації в")
    parser.add_argument("amount", type=float, default=100.0, help="Сума для конвертації")
    parser.add_argument("--start_date", type=str, default=None, help="Початкова дата (рік-місяць-день)")
    parser.add_argument("--save_to_file", action="store_true", help="Зберегти результат у файл")
    args = parser.parse_args()

    start_date = args.start_date if args.start_date else datetime.datetime.now().strftime('%Y-%m-%d')
    convert_currency(args.currency_from, args.currency_to, args.amount, start_date, args.save_to_file)

if __name__ == "__main__":
    main()