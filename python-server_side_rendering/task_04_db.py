#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# --- JSON oxuma ---
def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception:
        return []

# --- CSV oxuma ---
def read_csv(file_path):
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
            return data
    except Exception:
        return []

# --- SQLite oxuma ---
def read_sqlite():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        data = []
        for row in rows:
            data.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
        return data
    except Exception:
        return []

# --- Flask route ---
@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id', type=int)
    error = None
    data = []

    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    elif source == 'sql':
        data = read_sqlite()
    else:
        error = "Wrong source"

    if error is None and id_param is not None:
        filtered = [item for item in data if item['id'] == id_param]
        if not filtered:
            error = "Product not found"
        else:
            data = filtered

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
