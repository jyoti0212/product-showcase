from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load products (hardcoded or from JSON file)
def load_products():
    with open('products.json') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    product_list = load_products()
    return render_template('products.html', products=product_list)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product_list = load_products()
    product = next((p for p in product_list if p["id"] == product_id), None)
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)