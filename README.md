# Python bcrypt Login System

A simple authentication system written in Python using SQLite and bcrypt for secure password storage.

This project demonstrates how a basic login system works internally, including password hashing, login protection, password policies, and account management.

---

## Features

- User registration
- Secure password hashing using **bcrypt**
- Login authentication system
- Brute-force protection
- Account lock after multiple failed login attempts
- Password policy enforcement
- Email validation
- Password change functionality
- Logout functionality
- SQLite database storage

---

## Password Policy

Passwords must meet the following requirements:

- Minimum length of **8 characters**
- At least **one uppercase letter**
- At least **one number**
- At least **one special character**

---

## Security Features

- Passwords are securely stored using **bcrypt hashing**
- **Parameterized SQL queries** to prevent SQL injection
- **Login attempt tracking**
- **Temporary account lock** after 5 failed login attempts
- **Account lock duration: 10 minutes**

---

## Technologies Used

- **Python**
- **SQLite**
- **bcrypt**

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Selcuk58/python-bcrypt-login-system.git

## Installation

Navigate to the project folder:

cd python-bcrypt-login-system

Install the required dependency:

pip install bcrypt

---

## Usage

Run the program:

python main.py

The program will automatically create the database file users.db if it does not exist.

---

## How the System Works

1. A user registers with an email and password.
2. The password is hashed using bcrypt before being stored in the database.
3. During login, the entered password is compared with the stored password hash.
4. If too many incorrect login attempts occur, the account is temporarily locked.
5. After a successful login, the user can change their password or log out.

---

## Project Purpose

This project was created as a learning exercise to better understand:

- Authentication systems
- Secure password storage
- Brute-force protection mechanisms
- Database interaction in Python applications

---

## Author

Selcuk Demircan

---

## License

This project is intended for educational purposes.