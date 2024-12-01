# Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector
from datetime import datetime
from support import *

class Connection():

  def __init__(self):
    self.conn = mysql.connector.connect(user='gus',
                                        password='pass',
                                        host='localhost',
                                        port=3306,
                                        database='personal_library')
    self.cursor = self.conn.cursor()
  
  # This method will insert a group of books into the database.
  def insert_books(self, books_list):
      support = Support()
      # SQL query for inserting data into the books table
      self._SQL = """
      INSERT INTO books 
      (title, firstName, lastName, LC_Classifications, Publish_Date, Publisher, Subjects, Pagination, Info_URL, location)
      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
      """
      # Iterate through the books_list and insert each book
      for book in books_list:
        support.validate_and_handle_date(book)
        self.cursor.execute(self._SQL, (
            book["Title"],
            book['First Name'],
            book['Last Name'],
            book["LC Classifications"],
            book["Publish Date"],
            book["Publisher"],
            book["Subjects"],
            book["Pagination"],
            book["Info URL"],
            book['Location']
        ))
      # Commit all changes to the database
      self.conn.commit()
      print(f"{len(books_list)} books inserted successfully!")

