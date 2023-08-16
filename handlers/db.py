import sqlite3


db = sqlite3.connect("../bot.sqlite")
cursor = db.cursor()

def add_user(message):
    cursor.execute("SELECT id FROM users WHERE id=?",(message.from_user.id,))
    user = cursor.fetchone()
    if not user:
        cursor.execute("INSERT INTO users VALUES(?,?,?,?)", (message.from_user.id, "name", "team", "balance"))
        db.commit()
    else:
        return False

def add_user_name(message):
    cursor.execute("UPDATE users SET name=? WHERE id=?",(message.text,message.chat.id,))
    db.commit()

def add_user_team(message):
    cursor.execute("UPDATE users SET team=? WHERE id=?",(message.text,message.chat.id,))
    db.commit()

def get_user_name(user_id):
    cursor.execute("SELECT name FROM users WHERE id=?", (user_id,))
    user_name = cursor.fetchone()[0]
    return user_name

def get_user_team(user_id):
    cursor.execute("SELECT team FROM users WHERE id=?", (user_id,))
    user_team = cursor.fetchone()[0]
    return user_team