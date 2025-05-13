from flask import Flask, render_template, jsonify, abort
import json

app = Flask(__name__)

# Load product data
with open('products.json') as f:
    products = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def product_list():
    return render_template('products.html', products=products)

@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        abort(404)
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
