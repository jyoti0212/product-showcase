from flask import Flask, render_template
import json

app = Flask(__name__)

def load_products():
    with open('products.json') as f:
        return json.load(f)

@app.route('/')
def home():
    return render_template('index.html')  # optional homepage or redirect to /products

@app.route('/products')
def products():
    products = load_products()
    return render_template('products.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    products = load_products()
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('products_detail.html', product=product)
    else:
        return "Product not found", 404

if __name__ == '_main_':
    app.run(debug=True)