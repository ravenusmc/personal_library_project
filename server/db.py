# Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector
from datetime import datetime

class Connection():

  def __init__(self):
    self.conn = mysql.connector.connect(user='gus',
                                        password='pass',
                                        host='localhost',
                                        port=3306,
                                        database='personal_library')
    self.cursor = self.conn.cursor()
  
    
  def find_book_by_author(self, query):
    try:
        # Prepare the SQL query
        sql_query = """
            SELECT * FROM books 
            WHERE firstName LIKE %s OR lastName LIKE %s
        """
        # Using parameterized queries to prevent SQL injection
        like_query = f"%{query}%"
        self.cursor.execute(sql_query, (like_query, like_query))
        
        # Fetch all matching rows
        results = self.cursor.fetchall()
        # Return the results
        return results
    except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
  
  def find_book_by_title(self, query):
    try:
        # Prepare the SQL query
        sql_query = """
            SELECT * FROM books 
            WHERE Title LIKE %s
        """
        # Using parameterized queries to prevent SQL injection
        like_query = f"%{query}%"
        self.cursor.execute(sql_query, (like_query, ))
        
        # Fetch all matching rows
        results = self.cursor.fetchone()
        # Return the results
        return results
    except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
  
  def find_books_by_subject(self, query):
    try:
        # Prepare the SQL query
        sql_query = """
            SELECT * FROM books 
            WHERE Subjects LIKE %s
        """
        # Using parameterized queries to prevent SQL injection
        like_query = f"%{query}%"
        self.cursor.execute(sql_query, (like_query, ))
        
        # Fetch all matching rows
        results = self.cursor.fetchall()
        # Return the results
        return results
    except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
    

