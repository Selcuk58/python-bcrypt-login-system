import bcrypt
import sqlite3
import os
import string
import time




def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password_hash BLOB,
        login_attempts INTEGER NOT NULL DEFAULT 0,
        locked_until INTEGER NOT NULL DEFAULT 0
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
    current_time = int(time.time())
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
     return()
    cursor.execute(
    "SELECT locked_until FROM users WHERE email = ?",
    (eingabeEmail,)
    )
    lock_tuple = cursor.fetchone()
    lock_time1 = lock_tuple[0]
    if lock_time1 > current_time:
      print("Anmeldung nicht Möglich, versuchen Sie es später erneut")
      return
    if lock_time1 < current_time:
      cursor.execute(
      "UPDATE users SET login_attempts = 0, locked_until = 0 WHERE email = ?",
      (eingabeEmail,)
      )
      conn.commit()
       
    stored_hash = result[0]
    if bcrypt.checkpw(passwort_bytes, stored_hash):
      print("Login war Erfolgreich")
      cursor.execute(
       "UPDATE users SET login_attempts = 0 WHERE email = ?",
       (eingabeEmail,)
       )
      conn.commit()

    else:
      print("Passwort war leider falsch")
      cursor.execute(
      "UPDATE users SET login_attempts = login_attempts + 1 WHERE email = ?",
      (eingabeEmail,)
      )
      conn.commit()
      cursor.execute(
      "SELECT login_attempts FROM users WHERE email = ?",
      (eingabeEmail,)
      )
      tuple = cursor.fetchone()
      attempts = tuple[0]
      lock_time = current_time + 600
      if attempts > 5:
        cursor.execute(
        "UPDATE users SET locked_until = locked_until ? WHERE email = ?",
        (lock_time,eingabeEmail) 
        )
        conn.commit()
      else:
        return()
      

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

