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

  def encrypt_pass(self, post_data):
    password = post_data['password'].encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed
  
  # This method will insert a new user into the database.
  def insert(self, post_data, hashed):
      self._SQL = """insert into users
      (email, password)
      values
      (%s, %s)"""
      self.cursor.execute(self._SQL, (post_data['email'], hashed))
      self.conn.commit()
      user_created = True
      return user_created

  # This method will check to ensure that the username is in the database and then log them in.
  def verify_user(self, email, password):
        # Setting up a user dictionary
        user = {}
        # encoding the password to utf-8
        password = password.encode('utf-8')
        # Creating the query for the database
        query = ("""SELECT * FROM users WHERE email = %s""")
        self.cursor.execute(query, (email,))
        row = self.cursor.fetchone()
        # Here I check to see if the username is in the database.
        if str(row) == 'None':
            login_flag = False
            not_found = True
            password_no_match = False
        # If the user name is in the database I move here to check if the password
        # is valid.
        else:
            hashed = row[2].encode('utf-8')
            if bcrypt.checkpw(password, hashed):
                user["id"] = row[0]
                user['email'] = row[1]
                login_flag = True
                not_found = False
                password_no_match = False
            # This is a final catch all area. Basically if the password does not match
            # the user is not getting in.
            else:
                login_flag = False
                not_found = False
                password_no_match = True
        return login_flag, not_found, password_no_match, user  

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
    # Commit changes to the database
    self.conn.commit()
    db_obj = Connection()
    book_id = db_obj.get_book_id_last_book()
    return book_id
  
  def deleteBook(self, book_id):
    self._SQL = """
    DELETE FROM books
    WHERE book_id = %s
    """
    try:
        self.cursor.execute(self._SQL, (book_id, ))
        self.conn.commit()
        print(f"Book with ID {book_id} Deleted successfully.")
        return True
    except mysql.connector.Error as err:
        print("EXCEPT")
        print(f"Error: {err}")
        return False
  
  def get_book_id_last_book(self):
    self.cursor.execute("SELECT * FROM books ORDER BY book_id DESC LIMIT 1")
    last_book_added = self.cursor.fetchone()
    return last_book_added