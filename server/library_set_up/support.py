# This file will provide support methods
import re

class Support():

  # def validate_date(self, date_string):
  #   pattern = r"^\d{4}-\d{2}-\d{2}$"
  #   return bool(re.match(pattern, date_string))

  def validate_and_handle_date(self, book):
      """
      Validates and handles the 'Publish Date' field in the book dictionary.
      Converts valid years (e.g., '2021') to '2021-01-01'.
      Converts invalid dates ('N/A', empty strings, etc.) to None.
      """
      publish_date = book.get("Publish Date", "")
      
      # Check if Publish Date is empty or 'N/A'
      if publish_date in ["", "N/A", None]:
          book["Publish Date"] = None
          return
      
      # Check if it's a 4-digit year
      if isinstance(publish_date, str) and len(publish_date) == 4 and publish_date.isdigit():
          book["Publish Date"] = f"{publish_date}-01-01"  # Default to January 1st
          return

      # Validate full date (YYYY-MM-DD format)
      date_pattern = r"^\d{4}-\d{2}-\d{2}$"
      if not re.match(date_pattern, publish_date):
          # If invalid, set to None
          book["Publish Date"] = None
          return