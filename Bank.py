import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.load(fs)
        else:
            print("Database file not found, creating a new one.")
            data = []
    except Exception as err:
        print(f"Error loading data: {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            json.dump(cls.data, fs, indent=4)

    @staticmethod
    def __generate_account_no():
        alpha = random.choices(string.ascii_uppercase, k=3)
        num = random.choices(string.digits, k=3)
        acc_id = alpha + num
        random.shuffle(acc_id)
        return "".join(acc_id)

    @classmethod
    def __find_user(cls, account_no, pin):
        return next((u for u in cls.data if u['account_no'] == account_no and u['pin'] == pin), None)

    def create_account(self, name, age, email, pin):
        if age < 18:
            return f"You can create account after {18 - age} years."

        if not (pin.isdigit() and len(pin) == 4):
            return "PIN must be exactly 4 digits."

        account_no = self.__generate_account_no()
        new_user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": int(pin),
            "account_no": account_no,
            "balance": 0
        }

        Bank.data.append(new_user)
        self.__update()
        return f"Account created successfully! Your account no: {account_no}"

    def deposit_money(self, account_no, pin, amount):
        user = self.__find_user(account_no, pin)
        if not user:
            return "Invalid account or PIN."

        if amount <= 0:
            return "Deposit amount must be greater than 0."
        if amount > 10000:
            return "Cannot deposit more than 10,000 at once."

        user['balance'] += amount
        self.__update()
        return f"{amount} deposited successfully. New balance: {user['balance']}"

    def withdraw_money(self, account_no, pin, amount):
        user = self.__find_user(account_no, pin)
        if not user:
            return "Invalid account or PIN."
        if amount <= 0:
            return "Withdrawal amount must be greater than 0."
        if amount > 10000:
            return "Cannot withdraw more than 10,000 at once."
        if amount > user['balance']:
            return "Insufficient balance."

        user['balance'] -= amount
        self.__update()
        return f"{amount} withdrawn successfully. Remaining balance: {user['balance']}"

    def show_details(self, account_no, pin):
        user = self.__find_user(account_no, pin)
        if not user:
            return "Invalid account or PIN."
        return user

    def update_details(self, account_no, pin, name=None, email=None, new_pin=None):
        user = self.__find_user(account_no, pin)
        if not user:
            return "Invalid account or PIN."

        if name:
            user['name'] = name
        if email:
            user['email'] = email
        if new_pin and new_pin.isdigit() and len(new_pin) == 4:
            user['pin'] = int(new_pin)

        self.__update()
        return "Details updated successfully."

    def delete_account(self, account_no, pin):
        user = self.__find_user(account_no, pin)
        if not user:
            return "Invalid account or PIN."
        Bank.data.remove(user)
        self.__update()
        return "Account deleted successfully."
