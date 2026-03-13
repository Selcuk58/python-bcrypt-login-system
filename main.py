import bcrypt
import sqlite3
import os
import string

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password_hash BLOB
    )
    """)

    conn.commit()
    conn.close()

init_db()
print("Arbeitsverzeichnis:", os.getcwd())
def clear():
    os.system("cls")

def login():
    clear()
    print("Login")
    eingabeEmail = input("Gebe bitte deine Email ein")
    eingabePW = input("Bitte geben Sie ihr Passwort ein")
    passwort_bytes = eingabePW.encode()
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
    "SELECT password_hash FROM users WHERE email = ?",
    (eingabeEmail,))
    result = cursor.fetchone()
    if result is None:
     print("Emaíl Adresse oder Passwort stimmen nicht überein")
     clear()
     return()
    stored_hash = result[0]
    if bcrypt.checkpw(passwort_bytes, stored_hash):
      print("Login war Erfolgreich")
    else:
      print("Passwort war leider falsch")
      login()


def register():
    clear()
    email = input("Geben Sie bitte eine gültige Email Adresse an:")
    while True:
     passwort = input("Bitte Geben Sie ein Passwort an:")
     passwort1 = input("Bitte bestätigen Sie das Password:")
     if len(passwort) < 8:
      print("Dein Passwort muss mindestens 8 Zeichen haben")
      continue
     
     if not any(letter.isupper() for letter in passwort):
      print("Dein Passwort muss mindestens einen Großbuchstaben enthalten")
      continue
     if not any(letter.isdigit() for letter in passwort):
       print("Dein Passwort muss mindestens eine Zahl enthalten")
       continue
     if not any(letter in string.punctuation for letter in passwort):
       print("Dein Passwort muss mindestens ein Sonderzeichen enthalten")
       continue
     if passwort != passwort1:
        continue
     if passwort == passwort1:
      passwort_bytes = passwort.encode()
      salt = bcrypt.gensalt()
      hashed_passwort = bcrypt.hashpw(passwort_bytes, salt)
      conn = sqlite3.connect("users.db")
      cursor = conn.cursor()
      cursor.execute(
        "INSERT INTO users (email, password_hash) VALUES (?, ?)",
        (email, hashed_passwort))
      conn.commit()
      conn.close()
      print("Account wurde erfolgreich erstellt")
      menu()
      
     else:
        
      print("Passwörter stimmen nicht überein")
      menu()
    
     
def menu():
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = input("Wähle 1-3 aus ")
    if choice == "1":
     print("login gewählt")
     login()
    
    elif choice == "2":
     print("Register ausgewählt")
     register()

    elif choice == "3":
     exit()

    else:
     print("Ungültige Eingabe")




menu()

