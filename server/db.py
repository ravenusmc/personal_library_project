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
    print('herde')

