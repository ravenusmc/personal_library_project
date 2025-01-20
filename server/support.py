# This file will provide support methods to help in getting data. 
import requests
from bs4 import BeautifulSoup

class Support:

  @staticmethod
  def fetch_description(url):
      """
      Fetches the book description from the provided URL.
      """
      try:
          # Send a GET request to the URL
          response = requests.get(url)
          response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
          
          # Parse the HTML using BeautifulSoup
          soup = BeautifulSoup(response.text, 'html.parser')
          
          # Find the description in the div with class 'read-more__content'
          description_div = soup.find('div', class_='read-more__content')
          description = description_div.get_text(strip=True) if description_div else "Description not found."

          return description
      except requests.RequestException as e:
          print(f"Error fetching description: {e}")
          return "Failed to fetch description."



