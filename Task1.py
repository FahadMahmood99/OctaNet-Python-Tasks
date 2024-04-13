class Account:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds!")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Transferred: ${amount} to {recipient.user_id}")
            recipient.balance += amount
            recipient.transaction_history.append(f"Received: ${amount} from {self.user_id}")
        else:
            print("Insufficient funds!")

    def display_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)
        print(f"Current Balance: ${self.balance}")


class ATM:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, pin):
        if user_id not in self.users:
            self.users[user_id] = Account(user_id, pin)
            print("Account created successfully!")
        else:
            print("User ID already exists. Please choose a different one.")

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            print("Authentication successful!")
            return self.users[user_id]
        else:
            print("Invalid user ID or PIN.")
            return None


def main():
    atm = ATM()

    while True:
        print("\n1. Create Account\n2. Log In\n3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter User ID: ")
            pin = input("Enter PIN: ")
            atm.add_user(user_id, pin)
        elif choice == "2":
            user_id = input("Enter User ID: ")
            pin = input("Enter PIN: ")
            user = atm.authenticate_user(user_id, pin)
            if user:
                while True:
                    print("\n1. Deposit\n2. Withdraw\n3. Transfer\n4. Transaction History\n5. Quit")
                    option = input("Enter your choice: ")
                    if option == "1":
                        amount = float(input("Enter amount to deposit: "))
                        user.deposit(amount)
                    elif option == "2":
                        amount = float(input("Enter amount to withdraw: "))
                        user.withdraw(amount)
                    elif option == "3":
                        recipient_id = input("Enter recipient's User ID: ")
                        amount = float(input("Enter amount to transfer: "))
                        recipient = atm.users.get(recipient_id)
                        if recipient:
                            user.transfer(recipient, amount)
                        else:
                            print("Recipient not found.")
                    elif option == "4":
                        user.display_transaction_history()
                    elif option == "5":
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "3":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
