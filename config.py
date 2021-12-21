import sqlite3, os, datetime

DB_FILE = f'{os.getcwd()}/info.db'
LOG_FILE = f'{os.getcwd()}/log.txt'

def log(msg):
    with open(LOG_FILE, 'a') as f:
        f.write(msg)
        f.write('\n')

def init():
    conn  =sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    c.execute('CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, email TEXT)')
    conn.commit()

def id_exists(id_):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute('SELECT firstname FROM Users WHERE id=?', (id_,))
    results = c.fetchone()
    if results:
        return True
    else:
        return False

def email_exists(email):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute('SELECT firstname FROM Users WHERE email=?', (email,))
    results = c.fetchone()
    if results:
        return True
    else:
        return False

def get_data():
    conn  =sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    c.execute('SELECT * FROM Users')
    
    results = c.fetchall()

    if results:
        return results
    else:
        return []

def add_user(firstname, lastname, email):
    if firstname.strip() != "":
        if lastname.strip() != "":
            if email_exists(email) == False:
                try:
                    conn = sqlite3.connect(DB_FILE)
                    c = conn.cursor()

                    c.execute('INSERT INTO Users(firstname, lastname, email) VALUES(?, ?, ?)', (firstname, lastname, email))
                    conn.commit()
                    return True
                except Exception as e:
                    log(f'[{datetime.datetime.now()}] {e}')
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def delete_user(id_):
    if id_exists(id_):

        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()

        c.execute('DELETE FROM Users WHERE id = ?', (id_))
        conn.commit()
        return True
    else:
        return False
