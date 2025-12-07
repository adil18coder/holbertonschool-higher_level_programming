#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv(file_path):
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                # convert id and price to proper types
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
            return data
    except Exception:
        return []

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
    else:
        error = "Wrong source"

    if error is None:
        if id_param is not None:
            filtered = [item for item in data if item['id'] == id_param]
            if not filtered:
                error = "Product not found"
            else:
                data = filtered

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
