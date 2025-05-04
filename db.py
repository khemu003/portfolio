import mysql.connector
import os

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("PORT", 3306))
        )
        print("Connected to database successfully!")
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None
    
def Add_contact(name, email, message):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO contact (name, email, message) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, message))
    conn.commit()
    cursor.close()
    conn.close()