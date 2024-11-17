# This page I originally used to get to the book API: https://www.vinzius.com/post/free-and-paid-api-isbn/
# https://openlibrary.org/api/books?bibkeys=ISBN:9781523504381&jscmd=details&format=json

# The purpose of this file will be to 1. Get ISBN's into CSV file, 2. Use ISBN's, from CSV file 
# to get book information 3. put that book information into a new csv file. 
# I may want to add ISBN's to a CSV file that do not have information. 
import requests
import csv
import numpy as np
import pandas as pd

class BuildCSVFile():

  def __init__(self):
      self.data = pd.read_csv('books.csv')
  
  def place_ISBN_in_list(self):
      return self.data['ISBN'].tolist()

  def get_book_details(self, isbn_list):
    books_list = []
    for isbn in isbn_list:
      book_dictionary = {}
      url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=details&format=json"
      try:
          response = requests.get(url)
          response.raise_for_status()  # Raise an error for HTTP issues
          data = response.json()
          # Extract book details
          book_key = f"ISBN:{isbn}"
          if book_key in data:
              details = data[book_key].get("details", {})

              # Extract relevant details
              title = details.get("title", "N/A")
              authors = ', '.join([author.get("name", "N/A") for author in details.get("authors", [])])
              lc_classifications = ', '.join(details.get("lc_classifications", ["N/A"]))
              publish_date = details.get("publish_date", "N/A")
              publisher = ', '.join(details.get("publishers", ["N/A"]))
              subjects = ', '.join(details.get("subjects", ["N/A"]))
              pagination = details.get("pagination", "N/A")
              info_url = data[book_key].get("info_url", "N/A")

              # Populate the dictionary with the extracted book data
              book_dictionary["Title"] = title
              book_dictionary["Authors"] = authors
              book_dictionary["LC Classifications"] = lc_classifications
              book_dictionary["Publish Date"] = publish_date
              book_dictionary["Publisher"] = publisher
              book_dictionary["Subjects"] = subjects
              book_dictionary["Pagination"] = pagination
              book_dictionary["Info URL"] = info_url
              book_dictionary['Location'] = "A1"     
              books_list.append(book_dictionary)    
          else:
              print("No data found for the given ISBN.")
      except Exception as e:
          print(f"Error: {e}")
    return books_list
  
  def write_to_csv(self, data, filename="book_info.csv"):
    # Get the keys (column names) from the first dictionary
    headers = data[0].keys()
    # Write data to the CSV
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()  # Write the header row
        writer.writerows(data)  # Write all rows from the list of dictionaries    

  def run_program(self):
      program_obj = BuildCSVFile()
      isbn_list = program_obj.place_ISBN_in_list()
      books_list = program_obj.get_book_details(isbn_list)
      program_obj.write_to_csv(books_list)

book_object = BuildCSVFile()
book_object.run_program()


