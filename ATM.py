class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def authenticate_pin(self, entered_pin):
        return self.pin == entered_pin

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f'Withdrawn ${amount}')
            return True
        else:
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f'Deposited ${amount}')
            return True
        else:
            return False

    def transfer(self, amount, recipient):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f'Transferred ${amount} to {recipient.user_id}')
            return True
        else:
            return False

    def get_transaction_history(self):
        return self.transaction_history


class ATM:
    def __init__(self):
        self.users = {
            '123456': User('123456', '1234'),  # Example user, replace with actual user data
            # Add more users as needed
        }

    def start(self):
        print("Welcome to the ATM")
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")

        if user_id in self.users and self.users[user_id].authenticate_pin(pin):
            current_user = self.users[user_id]
            while True:
                print("\nPlease select an option:")
                print("1. Transactions History")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Transfer")
                print("5. Quit")
                choice = input("Enter your choice: ")

                if choice == '1':
                    print("Transaction History:")
                    for transaction in current_user.get_transaction_history():
                        print(transaction)
                
                elif choice == '2':
                    amount = float(input("Enter amount to withdraw: "))
                    if current_user.withdraw(amount):
                        print(f"${amount} withdrawn successfully")
                    else:
                        print("Withdrawal failed. Insufficient balance or invalid amount")
                
                elif choice == '3':
                    amount = float(input("Enter amount to deposit: "))
                    if current_user.deposit(amount):
                        print(f"${amount} deposited successfully")
                    else:
                        print("Deposit failed. Invalid amount")
                
                elif choice == '4':
                    recipient_id = input("Enter recipient's user ID: ")
                    amount = float(input("Enter amount to transfer: "))
                    if recipient_id in self.users:
                        recipient = self.users[recipient_id]
                        if current_user.transfer(amount, recipient):
                            print(f"${amount} transferred successfully to {recipient_id}")
                        else:
                            print("Transfer failed. Insufficient balance or invalid amount")
                    else:
                        print("Recipient not found")
                
                elif choice == '5':
                    print("Thank you for using the ATM. Goodbye!")
                    break
                
                else:
                    print("Invalid choice. Please try again.")
        
        else:
            print("Authentication failed. Invalid user ID or PIN.")

# Example usage
if __name__ == "__main__":
    atm = ATM()
    atm.start()
