# OOP-Encapsulation.py

# Bank Account System using Encapsulation (Python)
## Project Overview
This project demonstrates a simple **Bank Account System** using **Python Object-Oriented Programming (OOP)** with the concept of **Encapsulation**.
The program allows a user to:
- Check account balance
- Deposit money
- Withdraw money
The account balance is stored as a **private variable**, meaning it cannot be accessed directly from outside the class. This ensures better **data security and control**.

##  Features
- Create a bank account with an initial balance
- Deposit money into the account
- Withdraw money from the account
- Prevent withdrawal if balance is insufficient
- Prevent invalid withdrawal amounts
- Display current account balance
- Menu-driven interactive program
 
## Technologies Used
- Python
- Object-Oriented Programming (OOP)
  
## How the Program Works
### 1️ BankAccount Class
The program defines a class called **BankAccount** that manages account operations.
The account balance is stored as a **private variable**:
self.__balance
This means it cannot be accessed directly outside the class.

### 2️ Deposit Method
Adds money to the current balance.
Example:Deposit successful

### 3️ Withdraw Method
Allows the user to withdraw money.
Conditions:
- If amount ≤ 0 → Invalid amount
- If amount ≤ balance → Withdrawal successful
- If amount > balance → Insufficient balance

### 4️ Show Balance
Displays the current balance in the account.
Example:Current Balance: 1000

### 5️ Menu System
The program runs in a loop and provides options:

## Possible Improvements
Future improvements could include:
Multiple bank accounts
PIN authentication
Transaction history
File-based data storage
GUI interface using Tkinter

## Author
Harsha G
Learning Python | Embedded Systems | IoT
