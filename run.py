from flask import Flask, request, jsonify
from main import execute_query
app = Flask(__name__)


@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    start = request.form['start']
    rows = request.form['rows']
    result = execute_query(query, start, rows)

    return jsonify(result)

if __name__ == '__main__':
    app.run()