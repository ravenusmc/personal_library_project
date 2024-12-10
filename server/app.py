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
      if post_data['type'] == 'Author':
        author_results = db_obj.find_book_by_author(query)
      return jsonify(author_results)

if __name__ == '__main__':
    app.run(debug=True)