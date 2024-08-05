import sqlite3

def check_db():
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()

    # Verifique se a tabela 'user' existe e mostre seu conteúdo
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in database:", tables)

    if ('user',) in tables:
        cursor.execute("SELECT * FROM user;")
        users = cursor.fetchall()
        print("Users in database:", users)
    else:
        print("No 'user' table found.")

    conn.close()

if __name__ == "__main__":
    check_db()
