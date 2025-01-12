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

  
  def find_books_by_subject(self, query, description):
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
        # Return the results
        return results
    except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
  
  def find_books_by_location(self, query, description):
    try:
        # Prepare the SQL query
        sql_query = """
            SELECT * FROM books 
            WHERE location LIKE %s
        """
        # Using parameterized queries to prevent SQL injection
        like_query = f"%{query}%"
        self.cursor.execute(sql_query, (like_query, ))
        
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
        # Return the results
        return results
    except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
    
  def update_book(self, id_, firstName, lastName, location, publisher):
    query = """
        UPDATE books
        SET firstName = %s, lastName = %s, location = %s, publisher = %s
        WHERE book_id = %s
        """ 
    values = (firstName, lastName, location, publisher, id_)
    try:
        self.cursor.execute(query, values)
        self.conn.commit()
        print(f"Book with ID {id_} updated successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        self.cursor.close()
        self.conn.close()
  
  def add_book_to_database(self, book):
    # SQL query for inserting data into the books table
    self._SQL = """
    INSERT INTO books 
    (title, firstName, lastName, LC_Classifications, Publish_Date, Publisher, Subjects, Pagination, Info_URL, location)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    self.cursor.execute(self._SQL, (
          book["title"],
          book['firstName'],
          book['lastName'],
          book["lcClassifications"],
          book["publishDate"],
          book["publisher"],
          book["subjects"],
          book["pages"],
          book["infoUrl"],
          book['location']
      ))
    # Commit all changes to the database
    self.conn.commit()
    print('Book Insert! YAY!')
