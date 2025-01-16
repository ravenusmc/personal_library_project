from flask import Flask, jsonify, request
from flask_cors import CORS

# Importing files that I made:
from db import *

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Route to get books based on search query
@app.route('/getBooks', methods=['POST'])
def get_Books_Data():
  if request.method == 'POST':
    db_obj = Connection()
    post_data = request.get_json()
    query = post_data['query']
    description = post_data['description']
    if post_data['type'] == 'Author':
      results = db_obj.find_book_by_author(query, description)
    elif post_data['type'] == 'Title':
      results = db_obj.find_book_by_title(query, description)
    elif post_data['type'] == 'Subject': 
      results = db_obj.find_books_by_subject(query, description)
    else: 
      results = db_obj.find_books_by_location(query, description)
    return jsonify(results)

@app.route('/updateBook', methods=['POST'])
def updateBook():
  if request.method == 'POST': 
    db_obj = Connection()
    post_data = request.get_json()
    update_data = post_data['payload']['updateData']
    id_, firstName, lastName, location, publisher = update_data['id'], update_data['firstName'],update_data['lastName'], update_data['location'], update_data['publisher']
    db_obj.update_book(id_, firstName, lastName, location, publisher)
  return jsonify('5')

@app.route('/addBook', methods=['POST'])
def addBook():
  if request.method == 'POST':
    db_obj = Connection()
    post_data = request.get_json()
    book_data = post_data['book']
    db_obj.add_book_to_database(book_data)
  return jsonify('5')

@app.route('/deleteBook', methods=['POST'])
def deleteBook():
  if request.method == 'POST':
    db_obj = Connection()
    post_data = request.get_json()
    book_id = post_data['bookID']
    db_obj.deleteBook(book_id)
  return jsonify('5')

if __name__ == '__main__':
  app.run(debug=True)