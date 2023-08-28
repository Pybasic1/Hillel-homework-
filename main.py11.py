'''lesson11'''
import uuid
from decimal import Decimal
from datetime import datetime


class BankAccount:
    def __init__(self, account_name, initial_balance=0):
        self.account_name = account_name
        self.account_id = str(uuid.uuid4())
        self.balance = Decimal(initial_balance)
        self.transactions = []

    def deposit(self, amount):
        """Депозит коштів на рахунок."""
        if amount <= 0:
            return "Сума депозиту повинна бути більше нуля."

        self.balance += Decimal(amount)
        self._record_transaction(amount, "депозит")
        return f"{Decimal(amount)} було депоновано на рахунок."

    def withdraw(self, amount):
        """Виведення коштів з рахунку."""
        if amount <= 0:
            return "Сума виведення повинна бути більше нуля."

        if amount > self.balance:
            return "Недостатньо коштів на рахунку."

        self.balance -= Decimal(amount)
        self._record_transaction(amount, "виведення")
        return f"{Decimal(amount)} було виведено з рахунку."

    def get_balance(self):
        """Отримати поточний баланс."""
        return f"Поточний баланс рахунку {self.account_id}: {self.balance}"

    def _record_transaction(self, amount, transaction_type):
        """Записати транзакцію в список."""
        transaction = {
            "сума": Decimal(amount),
            "тип_операції": transaction_type,
            "поточна_дата": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.transactions.append(transaction)


if __name__ == "__main__":
    account = BankAccount("John Doe", 1000)
    print(account.deposit(500))
    print(account.withdraw(200))
    print(account.get_balance())