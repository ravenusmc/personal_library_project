# Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector
from datetime import datetime

# Bringing in libraries that I built. 
from support import *

class Connection():

  def __init__(self):
    self.conn = mysql.connector.connect(user='gus',
                                        password='pass',
                                        host='localhost',
                                        port=3306,
                                        database='personal_library')
    self.cursor = self.conn.cursor()
  
    
  def find_book_by_author(self, query, description):
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
        if results and description:
            updated_results = []
            for result in results: 
                # Assume the 9th element in the result is the URL
                url = result[9] if len(result) > 9 else None

                if url:
                    # Fetch the description using the Support class
                    support = Support()
                    description = support.fetch_description(url)
                    
                    # Append the description to the result
                    result = list(result)  # Convert tuple to list for modification
                    result.append(description)
                else:
                    result.append("No URL found in the result.")
                updated_results.append(result)
            return updated_results
        else:
            print("No book found matching the query.")
        return results
    except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
  
  def find_book_by_title(self, query, description):
    try:
        # Prepare the SQL query
        sql_query = """
            SELECT * FROM books 
            WHERE Title LIKE %s
        """
        # Using parameterized queries to prevent SQL injection
        like_query = f"%{query}%"
        self.cursor.execute(sql_query, (like_query, ))
        
        # Fetch the first matching row
        result = self.cursor.fetchone()
        if result and description:
            # Assume the 9th element in the result is the URL
            url = result[9] if len(result) > 9 else None
            if url:
                # Fetch the description using the Support class
                support = Support()
                description = support.fetch_description(url)
                # Append the description to the result
                result = list(result)  # Convert tuple to list for modification
                result.append(description)
            else:
                print("No URL found in the result.")
        else:
            print("No book found matching the query.")
        return result
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
    

