from flask import Flask, render_template, request
from search import search_rows
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        term = request.form['term']
        rows = search_rows(term)
        return render_template('index.html', rows=rows)
    if request.method == 'GET':
        return render_template('index.html', rows=[])
